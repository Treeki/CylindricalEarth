import "bootstrap"
import $ from "jquery"
import { identifySaveVersion, Schema, findOneMatchingType, SchemaType, loadSchema, Accessor, StructAccessor, PrimitiveAccessor, ArrayAccessor, TreeAccessor, gameData, setGameData } from "./data"
import { decryptSave } from "./crypto"
import "jquery.fancytree"
import "jquery.fancytree/dist/modules/jquery.fancytree.edit"
import "jquery.fancytree/dist/modules/jquery.fancytree.table"
import "./app.css"

interface FileStateMachineHandler {
	onShowAdvice: (text: string) => void
	onShowError: (text: string) => void
	onSaveFileLoaded: (header: File, body: File) => void
}

class FileStateMachine {
	pendingHeader: File|null = null
	pendingBody: File|null = null

	constructor(readonly handler: FileStateMachineHandler) {}

	dropFiles(files: FileList) {
		if (files.length >= 3) {
			this.handler.onShowError("That's too many files, I can't handle this!")
		} else if (files.length == 2) {
			// we expect a pair here
			const a = files[0], b = files[1]
			const aIsHeader = (a.size === 0x300), bIsHeader = (b.size === 0x300)
			if (aIsHeader != bIsHeader) {
				// successful
				this.pendingHeader = null
				this.pendingBody = null
				this.handler.onSaveFileLoaded(aIsHeader ? a : b, aIsHeader ? b : a)
			} else {
				this.handler.onShowError("Sorry, that's not right, you need to drop both the main file and the corresponding header file")
			}
		} else if (files.length == 1) {
			const file = files[0]
			if (file.size == 0x300) {
				if (this.pendingBody !== null) {
					this.handler.onSaveFileLoaded(file, this.pendingBody)
					this.pendingBody = null
				} else {
					this.handler.onShowAdvice("OK, now drop the other file...")
					this.pendingHeader = file
				}
			} else {
				if (this.pendingHeader !== null) {
					this.handler.onSaveFileLoaded(this.pendingHeader, file)
					this.pendingHeader = null
				} else {
					this.handler.onShowAdvice("OK, now drop the header file...")
					this.pendingBody = file
				}
			}
		}
	}
}



function loadAdvice(text: string) {
	$('#fileLoadError').hide()
	$('#fileLoadAdvice').show().text(text)
}
function loadAdviceAdd(text: string) {
	$('#fileLoadAdvice').append(' ' + text)
}
function loadError(text: string) {
	$('#fileLoadError').show().text(text)
}

let currentFileBuffer: [ArrayBuffer, ArrayBuffer]|null = null
let schema: Schema|null = null


function transformTree(acc: Accessor, name?: string): object {
	let obj: any = {
		title: acc.displayType,
		fieldName: name,
		accessor: acc
	}
	if (acc.hasChildren) {
		let tacc = acc as TreeAccessor
		obj.folder = true
		obj.children = []
		const count = tacc.displayChildrenCount
		for (let i = 0; i < count; i++)
			obj.children.push(transformTree(tacc.getChild(i), tacc.getChildTitle(i)))
	}
	return obj
}

function buildNodeChildren(accessor: Accessor): any {
	const children = []
	if (accessor.hasChildren) {
		const treeAcc = accessor as TreeAccessor
		const count = treeAcc.displayChildrenCount
		for (let i = 0; i < count; i++) {
			const childAcc = treeAcc.getChild(i)
			children.push({
				title: childAcc.displayType,
				fieldName: treeAcc.getChildTitle(i),
				accessor: childAcc,
				children: childAcc.hasChildren ? null : [],
				lazy: true
			})
			console
		}
	}
	return children
}
function expandNode(event: JQueryEventObject, data: Fancytree.EventData) {
	data.result = buildNodeChildren(data.node.data.accessor)
}


class EditContext {
	readonly tree: Fancytree.Fancytree
	readonly root: StructAccessor

	constructor(node: JQuery, readonly header: ArrayBuffer, readonly data: ArrayBuffer, offset: number, schema: Schema, type: SchemaType) {
		this.root = new StructAccessor(schema, new DataView(data), offset, type, 'root')
		this.tree = node.fancytree({
			source: buildNodeChildren(this.root),
			lazyLoad: expandNode,
			extensions: ['edit', 'table'],
			table: {nodeColumnIdx: 0, checkboxColumnIdx: -1, indentation: 24},
			icon: false,
			renderColumns: (event, data) => this._renderColumns(event, data)
		})
	}

	_renderColumns(event: JQueryEventObject, data: Fancytree.EventData) {
		const node = data.node
		const cols = node.tr.querySelectorAll('td')
		cols[1].textContent	= node.data.fieldName
		cols[2].textContent = node.data.accessor.displayValue
	}
}


let context: EditContext|null = null


async function loadHtml5FileAsync(headerFile: File, bodyFile: File) {
	loadAdvice('Loading your file...')
	const headerBuffer = await headerFile.arrayBuffer()
	const encBodyBuffer = await bodyFile.arrayBuffer()

	const headerVersion = identifySaveVersion(headerBuffer)
	if (headerVersion === null)
		throw "This header file looks invalid!"
	loadAdviceAdd(`Header is version ${headerVersion.codeA},${headerVersion.codeB}.`)

	if (headerVersion.encryptionMethod !== 2)
		throw `Unsupported encryption method ${headerVersion.encryptionMethod}!`

	const bodyBuffer = decryptSave(headerBuffer, encBodyBuffer)

	const bodyVersion = identifySaveVersion(bodyBuffer)
	if (bodyVersion === null)
		throw "This body file looks invalid!"
	loadAdviceAdd(`Body is version ${bodyVersion.codeA},${bodyVersion.codeB}.`)
	if (bodyVersion.codeA !== headerVersion.codeA || bodyVersion.codeB !== headerVersion.codeB)
		throw "Something doesn't look right here... Did you pick the correct pair of files?"

	loadAdviceAdd('Downloading the format file...')
	const schemaR = await fetch(`save_schema_${bodyVersion.codeA}_${bodyVersion.codeB}.json`)
	const schema = loadSchema(await schemaR.json())
	const type = findOneMatchingType(schema, bodyBuffer.byteLength)
	if (type === null)
		throw "I'm not sure what kind of savefile this is!"
	loadAdviceAdd(`This looks like a ${type.name}!`)

	if (gameData === undefined) {
		loadAdviceAdd('Downloading the game data file...')
		const gdR = await fetch('gameData.json')
		const gd = await gdR.json()
		setGameData(gd)
	}

	if (context !== null) {
		context.tree.widget.destroy()
		context = null
	}
	context = new EditContext($('#tree'), headerBuffer, bodyBuffer, 0, schema, type)
}

const fileStateMachine = new FileStateMachine({
	onShowAdvice: loadAdvice,
	onShowError: loadError,
	onSaveFileLoaded(header, body) {
		loadHtml5FileAsync(header, body).catch(loadError)
	}
})

function killEvent(e: Event) {
	e.stopPropagation()
	e.preventDefault()
}

document.body.addEventListener('dragenter', killEvent, false)
document.body.addEventListener('dragover', killEvent, false)
document.body.addEventListener('drop', e => {
	killEvent(e)
	const files = e.dataTransfer?.files
	if (files)
		fileStateMachine.dropFiles(files)
}, false)


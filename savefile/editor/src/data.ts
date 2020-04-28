import { utils } from "aes-js"
import { murmurHash3 } from "./crypto"

export interface SchemaField {
	id: number
	name: string
	type: number
	offset: number, size: number, alignment: number
	length: [number, number]
}

export interface SchemaType {
	name: string
	size: number, alignment: number
	fields: SchemaField[]
	fieldLookup: {[id: string]: SchemaField}
}

export interface SchemaPrimitive {
	name: string, size: number
}

export interface Schema {
	primitives: {[id: string]: SchemaPrimitive}
	types: {[id: string]: SchemaType}
}

export function loadSchema(json: any): Schema {
	const schema = json as Schema
	for (const id of Object.keys(schema.types)) {
		const type = schema.types[id]
		type.name = type.name.replace('::Game::', '')
		type.fieldLookup = {}
		for (const field of type.fields) {
			type.fieldLookup[field.id] = field
			type.fieldLookup[field.name] = field
		}
	}
	return schema
}

export function findOneMatchingType(schema: Schema, size: number): SchemaType|null {
	let candidate = null
	for (const id of Object.keys(schema.types)) {
		const type = schema.types[id]
		if (type.size === size) {
			if (candidate !== null)
				return null
			candidate = type
		}
	}
	return candidate
}


interface EventFlagMeta {
	id: number, enName: string, jpName: string
}
interface EventFlagWithMaxMeta extends EventFlagMeta {
	maximum: number
}

interface GameData {
	items: {[id: string]: string}
	fg: {[id: string]: {name: string, item: number}}
	outsidePartsLookup: {[id: string]: string}
	terrainUnits: {[id: string]: string}
	eventFlags: {
		aoc: EventFlagMeta[]
		bcat: EventFlagMeta[]
		house: EventFlagWithMaxMeta[]
		land: EventFlagWithMaxMeta[]
		landTemp: EventFlagWithMaxMeta[]
		npcMemory: EventFlagWithMaxMeta[]
		npcSave: EventFlagWithMaxMeta[]
		npcTemp: EventFlagWithMaxMeta[]
		playerActivity: EventFlagMeta[] // dunno what the max field is for this, yet
		player: EventFlagWithMaxMeta[]
		playerTemp: EventFlagWithMaxMeta[]
		playerVisit: EventFlagWithMaxMeta[]
		miles: EventFlagWithMaxMeta[]
		milesPlus: EventFlagMeta[]
	}
	villagerNames: {[id: string]: string}[]
	houseWallNames: {[id: string]: string}
	houseDoorNames: {[id: string]: string}
	houseRoofNames: {[id: string]: string}
}

export let gameData: GameData|undefined
export function setGameData(data: GameData) {
	gameData = data
}

function nameItemId(id: number): string {
	if (id in gameData!.items) {
		return gameData!.items[id]
	} else if (id === 0xFFFD) {
		return '<partial map item>'
	} else if (id === 0xFFFE) {
		return 'nothing'
	} else {
		return `<item ${id}>`
	}
}


const structPrettifiers: {[name: string]: ((acc: StructAccessor) => string|undefined)} = {}
const primitivePrettifiers: {[name: string]: ((acc: PrimitiveAccessor) => string|undefined)} = {}
const primitivePrettifiersName: {[name: string]: ((acc: PrimitiveAccessor) => string|undefined)} = {}
const customAccessorFactories: {[name: string]: ((schema: Schema, view: DataView, offset: number, type: SchemaType, name: string) => Accessor)} = {}

structPrettifiers['SaveMoney'] = acc => acc.getByName('Wallet')?.displayValue
structPrettifiers['s_ec65e7b4'] = acc => {
	const base = acc.getPrimByName('_71de9932')?.value
	const sub = acc.getPrimByName('_79d56a0c')?.value
	const shift = acc.getPrimByName('_d69168be')?.value
	const check = acc.getPrimByName('_c5b49f7e')?.value
	const byteSum = ((base >>> 24) & 0xff) + ((base >>> 16) & 0xff) + ((base >>> 8) & 0xff) + (base & 0xff)
	if (((byteSum - 45) & 0xff) == check) {
		// I suspect this needs fixing for some cases
		const shiftAmount = ((29 - shift) & 0x3f)
		const a = (base << shiftAmount) & 0xffffffff
		const b = (base >> (32 - shiftAmount)) & 0xffffffff
		const value = ((a + b + 0x80e32b11 - sub) & 0xffffffff) >>> 0
		return `🔒 ${value}`
	}
}

structPrettifiers['SaveWordTownName'] = acc => acc.getStructByName('TownName')?.getByName('Buffer')?.displayValue
structPrettifiers['SaveWordPlayerName'] = acc => acc.getStructByName('PlayerName')?.getByName('Buffer')?.displayValue
structPrettifiers['SaveLandId'] = acc => acc.getStructByName('Name')?.displayValue
structPrettifiers['SavePlayerBaseId'] = acc => acc.getStructByName('Name')?.displayValue
structPrettifiers['SavePlayerId'] = acc => {
	const player = acc.getStructByName('BaseId')?.displayValue
	const land = acc.getStructByName('LandId')?.displayValue
	return `${player} from ${land}`
}
structPrettifiers['SaveMyDesignNormal'] = acc => acc.getStructByName('Header')?.displayValue
structPrettifiers['SaveMyDesignPro'] = acc => acc.getStructByName('Header')?.displayValue
structPrettifiers['SaveMyDesignHeader'] = acc => {
	const title = acc.getStructByName('Title')?.getByName('Buffer')?.displayValue
	const player = acc.getStructByName('Author')?.displayValue
	return `${title} by ${player}`
}
structPrettifiers['SaveDate'] = acc => {
	const year = ('000' + acc.getByName('Year')?.displayValue).slice(-4)
	const month = ('0' + acc.getByName('Month')?.displayValue).slice(-2)
	const day = ('0' + acc.getByName('Day')?.displayValue).slice(-2)
	return `${year}-${month}-${day}`
}
structPrettifiers['SaveDateMD'] = acc => {
	const month = ('0' + acc.getByName('Month')?.displayValue).slice(-2)
	const day = ('0' + acc.getByName('Day')?.displayValue).slice(-2)
	return `${month}-${day}`
}
structPrettifiers['SaveTime'] = acc => {
	const cal = acc.getByName('Calendar')
	if (cal !== undefined) {
		const calp = cal as PrimitiveAccessor
		const year = ('000' + calp.view.getUint16(calp.offset, true)).slice(-4)
		const month = ('0' + calp.view.getUint8(calp.offset + 2)).slice(-2)
		const day = ('0' + calp.view.getUint8(calp.offset + 3)).slice(-2)
		const hour = ('0' + calp.view.getUint8(calp.offset + 4)).slice(-2)
		const minute = ('0' + calp.view.getUint8(calp.offset + 5)).slice(-2)
		const second = ('0' + calp.view.getUint8(calp.offset + 6)).slice(-2)
		return `${year}-${month}-${day} ${hour}:${minute}:${second}`
	}
}
structPrettifiers['SaveItemName'] = acc => {
	const id = acc.getPrimByName('UniqueID')?.value
	if (id !== undefined)
		return nameItemId(id)
}
structPrettifiers['SaveAnimal'] = acc => {
	const name = acc.getByName('Id')?.displayValue
	const date = acc.getByName('BirthDate')?.displayValue
	if (name !== undefined && !name.startsWith('👻'))
		return `${name} (since ${date})`
}
structPrettifiers['FtrData'] = acc => {
	const name = acc.getByName('ItemName')?.displayValue
	const x = acc.getPrimByName('UnitZ')?.value
	const y = acc.getPrimByName('UnitZ')?.value
	const direction = acc.getPrimByName('Direction')?.value
	return `${name} at (${x},${y}), ${direction*90}°`
}

const speciesEmoji = [
	'🐜', '🐻', '🐦', '🐂', '🐈', '🐻', '🐓', '🐄',
	'🐊', '🦌', '🐶', '🦆', '🐘', '🐸', '🐐', '🦍',
	'🐹', '🦛', '🐴', '🐨', '🦘', '🦁', '🐒', '🐭',
	'🐙', '🐦', '🦅', '🐧', '🐷', '🐰', '🦏', '🐑',
	'🐿', '🐯', '🐺'
]

primitivePrettifiers['Game::NpcNormalID'] = acc => {
	const species = acc.view.getUint8(acc.offset)
	const whom = acc.view.getUint8(acc.offset+1)
	const unk = acc.view.getUint8(acc.offset+2)
	const hash = gameData!.villagerNames[species]
	if (hash !== undefined && whom in hash)
		return `${speciesEmoji[species]} ${hash[whom]}`
	else
		return `👻 ${species},${whom},${unk}`
}
primitivePrettifiers['V3f'] = acc => {
	const x = acc.view.getFloat32(acc.offset, true)
	const y = acc.view.getFloat32(acc.offset+4, true)
	const z = acc.view.getFloat32(acc.offset+8, true)
	return `{${x},${y},${z}}`
}
primitivePrettifiersName['WallUniqueID'] = primitivePrettifiersName['OrderWallUniqueID'] = acc => {
	return gameData?.houseWallNames[acc.value]
}
primitivePrettifiersName['RoofUniqueID'] = primitivePrettifiersName['OrderRoofUniqueID'] = acc => {
	return gameData?.houseRoofNames[acc.value]
}
primitivePrettifiersName['DoorUniqueID'] = primitivePrettifiersName['OrderDoorUniqueID'] = acc => {
	return gameData?.houseDoorNames[acc.value]
}


export interface Accessor {
	displayType: string
	displayValue: string
	hasChildren: boolean
}

export interface TreeAccessor extends Accessor {
	displayChildrenCount: number
	getChild(index: number): Accessor
	getChildTitle(index: number): string
}

export interface EditableAccessor extends Accessor {
	getEditableStr(): string
	setEditableStr(str: string): void
}


export class PrimitiveAccessor implements EditableAccessor {
	constructor(readonly view: DataView, readonly offset: number, readonly type: SchemaPrimitive, readonly name: string) {
	}

	get value(): any {
		switch (this.type.name) {
			case 'u8': return this.view.getUint8(this.offset)
			case 'u16': return this.view.getUint16(this.offset, true)
			case 'u32': return this.view.getUint32(this.offset, true)
			case 'u64': return [this.view.getUint32(this.offset + 4, true), this.view.getUint32(this.offset, true)]
			case 's8': return this.view.getInt8(this.offset)
			case 's16': return this.view.getInt16(this.offset, true)
			case 's32': return this.view.getInt32(this.offset, true)
			case 's64': return [this.view.getInt32(this.offset + 4, true), this.view.getInt32(this.offset, true)]
			case 'f32': return this.view.getFloat32(this.offset, true)
			case 'f64': return this.view.getFloat64(this.offset, true)
			case 'bool': return (this.view.getUint8(this.offset) != 0)
			case 'char': return this.view.getUint8(this.offset)
			case 'char16': return this.view.getUint16(this.offset, true)
			default: return new Uint8Array(this.view.buffer, this.view.byteOffset + this.offset, this.type.size)
		}
	}

	getEditableStr(): string {
		const v = this.value
		if (v instanceof Uint8Array)
			return utils.hex.fromBytes(v)
		else
			return v.toString()
	}
	setEditableStr(str: string): void {
		switch (this.type.name) {
			case 'char': case 'u8': this.view.setUint8(this.offset, parseInt(str)); break
			case 'char16': case 'u16': this.view.setUint16(this.offset, parseInt(str), true); break
			case 'u32': this.view.setUint32(this.offset, parseInt(str) >>> 0, true); break
			case 'u64':
				const a = eval(str) // lmao this is bad
				this.view.setUint32(this.offset + 4, a[0] >>> 0, true)
				this.view.setUint32(this.offset, a[1] >>> 0, true)
				break
			case 's8': this.view.setInt8(this.offset, parseInt(str)); break
			case 's16': this.view.setInt16(this.offset, parseInt(str), true); break
			case 's32': this.view.setInt32(this.offset, parseInt(str) >>> 0, true); break
			case 's64':
				const a_ = eval(str) // lmao this is bad
				this.view.setInt32(this.offset + 4, a_[0], true)
				this.view.setInt32(this.offset, a_[1], true)
				break
			case 'f32': this.view.setFloat32(this.offset, parseFloat(str), true); break
			case 'f64': this.view.setFloat64(this.offset, parseFloat(str), true); break
			case 'bool': this.view.setUint8(this.offset, (str == 'true') ? 1 : 0); break
			default:
				const newData = utils.hex.toBytes(str)
				if (newData.byteLength === this.type.size) {
					const buf = new Uint8Array(this.view.buffer, this.view.byteOffset + this.offset, this.type.size)
					buf.set(newData, 0)
				} else {
					alert('bad size')
				}
				break
		}
	}

	hasChildren = false
	get displayType(): string {
		return this.type.name
	}
	get displayValue(): string {
		if (this.name in primitivePrettifiersName) {
			const v = primitivePrettifiersName[this.name](this)
			if (v !== undefined) return v
		}
		if (this.type.name in primitivePrettifiers) {
			const v = primitivePrettifiers[this.type.name](this)
			if (v !== undefined) return v
		}

		const v = this.value
		if (v instanceof Uint8Array)
			return utils.hex.fromBytes(v)
		else
			return v.toString()
	}
}

export class StructAccessor implements TreeAccessor {
	constructor(readonly schema: Schema, readonly view: DataView, readonly offset: number, readonly type: SchemaType, readonly name: string) {
	}

	get fields(): SchemaField[] {
		return this.type.fields
	}

	getField(field: SchemaField): Accessor {
		if (field.length[0] > 1 || field.length[1] > 1) {
			if (field.type in this.schema.primitives) {
				return new PrimitiveArrayAccessor(
					this.schema, this.view, this.offset + field.offset,
					this.schema.primitives[field.type], field.length, field.name)
			} else {
				return new ArrayAccessor(
					this.schema, this.view, this.offset + field.offset,
					this.schema.types[field.type], field.length, field.name)
			}
		} else {
			if (field.type in this.schema.primitives) {
				const prim = this.schema.primitives[field.type]
				return new PrimitiveAccessor(this.view, this.offset + field.offset, prim, field.name)
			} else {
				const type = this.schema.types[field.type]
				if (type.name in customAccessorFactories)
					return customAccessorFactories[type.name](this.schema, this.view, this.offset + field.offset, type, field.name)
				else
					return new StructAccessor(this.schema, this.view, this.offset + field.offset, type, field.name)
			}
		}
	}
	getByName(name: string): Accessor|undefined {
		const field = this.type.fieldLookup[name]
		if (field !== undefined)
			return this.getField(field)
	}
	getStructByName(name: string): StructAccessor|undefined {
		const acc = this.getByName(name)
		if (acc !== undefined && 'fields' in acc)
			return acc
	}
	getPrimByName(name: string): PrimitiveAccessor|undefined {
		const acc = this.getByName(name)
		if (acc !== undefined && acc instanceof PrimitiveAccessor)
			return acc
	}

	get displayType(): string {
		return this.type.name
	}
	get displayValue(): string {
		// handle special one-field structs
		if (this.type.fields.length === 1) {
			const field = this.type.fields[0]
			if (field.size === 4 && this.schema.primitives[field.type]?.name === 's32') {
				const enumValue = (this.getField(field) as PrimitiveAccessor).value
				return `<Enum: ${enumValue}>`
			}
		}

		if (this.type.name in structPrettifiers) {
			const v = structPrettifiers[this.type.name](this)
			if (v !== undefined) return v
		}

		return '<...>'
	}

	hasChildren = true
	get displayChildrenCount(): number { return this.type.fields.length }
	getChild(index: number) { return this.getField(this.type.fields[index]) }
	getChildTitle(index: number) { return this.type.fields[index].name }
}

export class ArrayAccessor implements TreeAccessor {
	constructor(
		readonly schema: Schema,
		readonly view: DataView,
		readonly offset: number,
		readonly type: SchemaType|SchemaPrimitive,
		readonly length: [number,number],
		readonly name: string
	) {
	}

	hasChildren = true
	get displayChildrenCount(): number { return this.length[0] }
	getChild(i: number): Accessor {
		if (this.length[1] > 1) {
			// two levels deep
			const stride = this.type.size * this.length[1]
			const offset = this.offset + i * stride
			return new ArrayAccessor(this.schema, this.view, offset, this.type, [this.length[1], 0], this.name)
		} else {
			// just one level deep
			const stride = this.type.size
			const offset = this.offset + i * stride
			if ('fields' in this.type) {
				return new StructAccessor(this.schema, this.view, offset, this.type, this.name)
			} else {
				return new PrimitiveAccessor(this.view, offset, this.type, this.name)
			}
		}
	}
	getChildTitle(i: number): string { return `[${i}]` }

	get displayType(): string {
		if (this.length[1] > 1) {
			return `${this.type.name}[${this.length[0]}][${this.length[1]}]`
		} else {
			return `${this.type.name}[${this.length[0]}]`
		}
	}
	get displayValue(): string {
		return "[...]"
	}
}

export class PrimitiveArrayAccessor extends ArrayAccessor {
	constructor(
		readonly schema: Schema,
		readonly view: DataView,
		readonly offset: number,
		readonly type: SchemaPrimitive,
		readonly length: [number, number],
		readonly name: string
	) {
		super(schema, view, offset, type, length, name)
	}

	hasChildren = false

	get displayValue(): string {
		const totalLen = this.length[0] * this.length[1]
		if (this.type.name == 'char16') {
			const codepoints = new Uint16Array(this.view.buffer, this.view.byteOffset + this.offset, totalLen)
			return String.fromCodePoint(...codepoints)
		} else {
			const bits = []
			const threshold = 16
			for (let i = 0; i < threshold && i < totalLen; i++)
				bits.push(this.getChild(i).displayValue)
			if (totalLen > threshold)
				bits.push('...')
			return `[${bits.join(', ')}]`
		}
	}
}


export class EventFlagAccessor implements EditableAccessor {
	constructor(readonly view: DataView, readonly offset: number, readonly flag: EventFlagMeta|EventFlagWithMaxMeta, readonly is8bit: boolean) {
	}

	hasChildren = false
	get displayType(): string { return this.flag.jpName }
	get displayValue(): string {
		const value = this.is8bit ? this.view.getUint8(this.offset) : this.view.getUint16(this.offset, true)
		if ('maximum' in this.flag) {
			if (this.flag.maximum == 1)
				return (value == 0) ? 'false' : 'true'
		}
		return value.toString()
	}

	getEditableStr(): string {
		return this.displayValue
	}
	setEditableStr(str: string) {
		let value
		if ('maximum' in this.flag && this.flag.maximum == 1)
			value = (str == 'true') ? 1 : 0
		else
			value = parseInt(str)
		if (this.is8bit)
			this.view.setUint8(this.offset, value)
		else
			this.view.setUint16(this.offset, value, true)
	}
}

export class EventFlagsAccessor implements TreeAccessor {
	flags: EventFlagMeta[]

	constructor(
		readonly schema: Schema,
		readonly view: DataView,
		readonly offset: number,
		readonly type: SchemaPrimitive,
		readonly name: string,
		readonly key: keyof GameData['eventFlags'],
		readonly is8bit: boolean = false
	) {
		this.flags = gameData!.eventFlags[key]
		console.log(this.flags)
	}

	hasChildren = true
	get displayChildrenCount(): number { return this.flags.length }
	get displayType(): string { return this.type.name }
	get displayValue(): string { return `<${this.flags.length} flags>` }
	getChild(index: number): Accessor {
		const sz = this.is8bit ? 1 : 2
		return new EventFlagAccessor(this.view, this.offset + sz * this.flags[index].id, this.flags[index], this.is8bit)
	}
	getChildTitle(index: number): string { return this.flags[index].enName }
}

customAccessorFactories['SaveEventFlagHouse'] = (schema, view, offset, type, name) => {
	return new EventFlagsAccessor(schema, view, offset, type, name, 'house')
}
customAccessorFactories['SaveEventFlagLand'] = (schema, view, offset, type, name) => {
	return new EventFlagsAccessor(schema, view, offset, type, name, 'land')
}
customAccessorFactories['SaveEventFlagLandTemp'] = (schema, view, offset, type, name) => {
	return new EventFlagsAccessor(schema, view, offset, type, name, 'landTemp')
}
customAccessorFactories['SaveEventFlagNpcMemory'] = (schema, view, offset, type, name) => {
	return new EventFlagsAccessor(schema, view, offset, type, name, 'npcMemory', true)
}
customAccessorFactories['SaveEventFlagNpcSave'] = (schema, view, offset, type, name) => {
	return new EventFlagsAccessor(schema, view, offset, type, name, 'npcSave')
}
customAccessorFactories['SaveEventFlagNpcTemp'] = (schema, view, offset, type, name) => {
	return new EventFlagsAccessor(schema, view, offset, type, name, 'npcTemp')
}
customAccessorFactories['SaveEventFlagPlayer'] = (schema, view, offset, type, name) => {
	return new EventFlagsAccessor(schema, view, offset, type, name, 'player')
}
customAccessorFactories['SaveEventFlagPlayerTemp'] = (schema, view, offset, type, name) => {
	return new EventFlagsAccessor(schema, view, offset, type, name, 'playerTemp')
}
customAccessorFactories['SaveEventFlagPlayerVisit'] = (schema, view, offset, type, name) => {
	return new EventFlagsAccessor(schema, view, offset, type, name, 'playerVisit')
}



interface ACSaveVersion {
	codeA: number, codeB: number, encryptionMethod: number
}

export function identifySaveVersion(body: ArrayBuffer): ACSaveVersion|null {
	if (body.byteLength < 0x100)
		return null
	const dv = new DataView(body)
	return {
		codeA: dv.getUint32(4, true),
		codeB: dv.getUint32(0, true),
		encryptionMethod: dv.getUint16(0xC, true)
	}
}


export function updateHashes(body: ArrayBuffer, offset: number, type: SchemaType, schema: Schema) {
	// console.log(`updates for ${type.name}`)
	for (let i = type.fields.length - 1; i >= 0; i--) {
		const field = type.fields[i]
		// console.log(`looking at ${field.name}`)
		if (field.id === 0xd35a9251) {
			// this is a hash that needs updating
			const hashStart = offset + field.offset + 4
			const hashEnd = offset + type.size
			const hashData = new Uint32Array(body, hashStart, (hashEnd - hashStart) >> 2)
			const dv = new DataView(body, offset + field.offset, 4)
			const existingHash = dv.getUint32(0, true)
			const newHash = murmurHash3(hashData)
			if (existingHash === newHash) {
				console.log(`no change in hash for ${type.name}`)
			} else {
				console.log(`hash for ${type.name} updated`)
				dv.setUint32(0, newHash, true)
			}
		} else if (field.type in schema.types) {
			// do the old nested update
			const count = field.length[0] * field.length[1]
			const fieldType = schema.types[field.type]
			if (fieldType.name === 'SaveProfileJPEG')
				continue // this breaks things fsr
			for (let j = 0; j < count; j++)
				updateHashes(body, offset + field.offset + (j * fieldType.size), fieldType, schema)
		}
	}
}


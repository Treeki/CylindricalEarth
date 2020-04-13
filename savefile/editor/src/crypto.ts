import "aes-js"
import {ModeOfOperation, Counter} from "aes-js"

// https://stackoverflow.com/a/6422061
function mult32(a: number, b: number) {
	const ah = (a >>> 16) & 0xFFFF, al = (a & 0xFFFF)
	const bh = (b >>> 16) & 0xFFFF, bl = (b & 0xFFFF)
	const high = ((ah * bl) + (al * bh)) & 0xFFFF
	return ((high << 16) >>> 0) + (al * bl)
}

class SeadRandom {
	_a: number
	_b: number
	_c: number
	_d: number

	constructor(initial?: number | number[]) {
		if (initial === undefined)
			initial = 42069

		if (typeof(initial) === 'number') {
			this._a = (mult32(0x6c078965, initial ^ (initial >>> 30)) + 1) >>> 0
			this._b = (mult32(0x6c078965, this._a ^ (this._a >>> 30)) + 2) >>> 0
			this._c = (mult32(0x6c078965, this._b ^ (this._b >>> 30)) + 3) >>> 0
			this._d = (mult32(0x6c078965, this._c ^ (this._c >>> 30)) + 4) >>> 0
		} else {
			this._a = initial[0]
			this._b = initial[1]
			this._c = initial[2]
			this._d = initial[3]
		}
	}

	getU32(): number {
		const n = this._a ^ (this._a << 11)
		this._a = this._b
		this._b = this._c
		this._c = this._d
		this._d = n ^ (n >>> 8) ^ this._d ^ (this._d >>> 19)
		return (this._d >>> 0)
	}
}

function pullBytes(seedData: Uint32Array, offset: number): Uint8Array {
	const rng = new SeadRandom(seedData[seedData[offset] & 0x7F])
	const skip = (seedData[seedData[offset + 1] & 0x7F] & 0xF) + 1
	for (let i = 0; i < (skip * 2); i++)
		rng.getU32()
	const result = new Uint8Array(16)
	for (let i = 0; i < 16; i++)
		result[i] = rng.getU32() >>> 24
	return result
}

export function decryptSave(header: ArrayBuffer, body: ArrayBuffer): ArrayBuffer {
	const seedData = new Uint32Array(header, 0x100)
	const key = pullBytes(seedData, 0)
	const iv = pullBytes(seedData, 2)

	return new ModeOfOperation.ctr(key, new Counter(iv)).decrypt(new Uint8Array(body)).buffer
}

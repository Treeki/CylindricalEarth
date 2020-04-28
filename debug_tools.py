from pynoexs import *
from functools import cached_property
import mmh3

stages = 'AmiiboTelephone CharacterOrder DateCheck Dream_Tkk GrowUp GrowUpPlayerSwitch GrowUpSharePlayForceBreakup ' + \
 'GrowUpTalk IdrAirPort IdrAirPortDemoDeparture IdrAirPortDemoRetire IdrAirPortDemoVisitor IdrCampSiteTent ' + \
 'IdrMarket01 IdrMarket02 IdrMuseumEnt00 IdrMuseumEnt01 IdrMuseumFish_0 IdrMuseumFish_1 IdrMuseumFish_2 ' + \
 'IdrMuseumFossil_0 IdrMuseumFossil_1 IdrMuseumFossil_2 IdrMuseumInsect_0 IdrMuseumInsect_1 IdrMuseumInsect_2 ' + \
 'IdrOffice01 IdrTailor IdrTanukichi MainField MainFieldDemoCeremony MainFieldDemoFirstLive MainFieldDemoLanding ' + \
 'MainFieldDemoLandingNet MyDesignExchange MysteryTourIsland NetDemo OpeningMovie PhotoStudio PhotoStudioIsland ' + \
 'SaveGameClose Title'
stageHashes = {}
def addStageHash(s):
    h = mmh3.hash(s.encode('ascii')) & 0xffffffff
    stageHashes[h] = s
for s in stages.split(' '): addStageHash(s)
for i in range(10): addStageHash(f'NpcHouse{i}')
for i in range(5): addStageHash(f'PhotoStudio_{i+1}')
for i in range(8):
    addStageHash(f'PlayerHouse{i}')
    for j in range(5):
        addStageHash(f'PlayerHouse{i}_{j+1}')


def find_ACNH(nx):
    for pid in reversed(nx.get_pids()):
        if nx.get_title_id(pid) == 0x1006f8002326000:
            return pid
    return None


def derefObjPtr(cls, addr):
    p = ptr(addr)
    if p > 0:
        return cls(p)

def derefObjPtrList(cls, addr, amount, step=8):
    buf = read(addr, amount * step)
    results = [None] * amount
    for i in range(amount):
        p = struct.unpack_from('<Q', buf, i * step)[0]
        if p > 0:
            results[i] = cls(nx_to_re(p))
    return results


class SaveMgr:
    @classmethod
    def get(cls):
        addr = ptr(0x710373c1f8) # 1.1.4
        return SaveMgr(addr)

    def __init__(self, base):
        self.base = base

    @property
    def muxFlags(self): return u8(self.base + 0x26b2b)

    @property
    def main(self): return ptr(self.base + 0x10)
    @property
    def personal(self): return ptr(self.base + 0x28)

    @property
    def landStore(self): return ptr(self.base + 0xc0) + 0x70


class FieldSystem:
    @classmethod
    def get(cls):
        addr = ptr(0x71035a6fd8) # 1.1.4
        return FieldSystem(addr)

    def __init__(self, base):
        self.base = base

    @property
    def fields(self): return derefObjPtrList(Field, self.base + 0x28 + 8, 50)
    @property
    def defaultField(self): return derefObjPtr(Field, self.base + 0x28 + 0x198)


class Field:
    def __init__(self, base):
        self.base = base

    def __repr__(self):
        return f'<Field {self.name} area={self.fullArea} editable={self.editableArea}>'

    @cached_property
    def name(self):
        try:
            return stageHashes[self.nameHash]
        except KeyError:
            return '(unknown %08x)' % self.nameHash
    @cached_property
    def nameHash(self): return u32(self.base + 0x180)
    @cached_property
    def fullArea(self): return readRectHU(self.base + 0x10)
    @cached_property
    def editableArea(self): return readRectHU(self.base + 0x38)

    @property
    def itemLayers(self): return derefObjPtrList(ItemLayer, self.base + 0xc8 + 8, 8, 0x10)


class Item:
    def __init__(self, data, offset=0):
        self.uniqueID, self.system, self.additional, self.free = struct.unpack_from('<HBBI', data, offset)

    def __repr__(self):
        return f'<Item {self.uniqueID:5d} / {self.system:02x} / {self.additional:02x} / {self.free:08x}>'

    def __eq__(self, other):
        return self.uniqueID == other.uniqueID and \
               self.system == other.system and \
               self.additional == other.additional and \
               self.free == other.free


class ItemLayer:
    def __init__(self, base):
        self.base = base

        # this is kinda tricky because of the indirection
        # involved in the real code, we can't just fetch
        # a pointer -- it goes through multiple virtual methods
        fetchDelegateVT = ptr(self.base + 0x28)
        if fetchDelegateVT == 0x7103185398:
            func = ptr(self.base + 0x28 + 8)
            if func == 0x7100589050:
                # mainfield bottom item layer backingstore
                store = SaveMgr.get().landStore + 0x1575e8 + 0x38 + 0x38
                size = 0xe0,0xc0
            elif func == 0x7100589070:
                # mainfield top item layer backingstore
                store = SaveMgr.get().landStore + 0x1575e8 + 0xa8 + 0x38
                size = 0xe0,0xc0

        self.store = store
        self.width, self.height = size
        self.buffer = ptr(store + 8) + u64(store + 0x10)

    def __repr__(self):
        return f'<ItemLayer @ {self.base:x}>'

    @cached_property
    def tags(self):
        return derefObjPtr(ItemTag2D, self.base + 0x18)

    def __getitem__(self, key):
        x, y = key
        offset = self.height * x + y
        return Item(read(self.buffer + offset * 8, 8))

    @property
    def all(self):
        w, h = self.width, self.height
        amount = self.width * self.height
        buf = read(self.buffer, amount * 8)
        return [[Item(buf, (h * x + y) * 8) for x in range(w)] for y in range(h)]


class ItemTag2D:
    def __init__(self, base):
        self.base = base

    @cached_property
    def width(self): return u32(self.base + 8)
    @cached_property
    def height(self): return u32(self.base + 0xc)
    @cached_property
    def buffer(self): return ptr(self.base + 0x10)

    def __getitem__(self, key):
        x, y = key
        offset = self.width * y + self.height
        return u32(self.buffer + offset * 4)

    @property
    def all(self):
        amount = self.width * self.height
        buf = read(self.buffer, amount * 4)
        return [struct.unpack_from(f'<{self.width}I', buf, i * self.width * 4) for i in range(self.height)]

    @property
    def nonZeroTagIterator(self):
        for y, row in enumerate(self.all):
            for x, val in enumerate(row):
                if val > 0:
                    yield x,y,val


nx = NoexsClient(('192.168.0.121', 7331))
nx.attach(find_ACNH(nx))
print(nx.get_status())

# find our binary
code_static_rx = []
code_static_r = []
code_mutable = []
for addr,size,typ,perm in nx.get_memory_info():
    #print('%10x %10x %d %r' % (addr,size,perm,typ))
    if typ == MemoryType.CODE_STATIC:
        if perm == 5:
            code_static_rx.append((addr,size))
        elif perm == 1:
            code_static_r.append((addr,size))
    elif typ == MemoryType.CODE_MUTABLE:
        code_mutable.append((addr, size))

text, rodata, data = code_static_rx[1], code_static_r[1], code_mutable[1]
print('TEXT: %10x .. %10x' % text)
print('RODATA: %10x .. %10x' % rodata)
print('DATA: %10x .. %10x' % data)

# now we want to work with pointers in the form Ghidra shows...
ptr_adjust = 0x7100000000 - text[0]
def nx_to_re(p): return p + ptr_adjust
def re_to_nx(p): return p - ptr_adjust

def ptr(re_p):
    value = nx.peek64(re_to_nx(re_p))
    return 0 if value == 0 else nx_to_re(value)
def u64(re_p): return nx.peek64(re_to_nx(re_p))
def f32(re_p): return struct.unpack('<f', struct.pack('<I', nx.peek32(re_to_nx(re_p))))[0]
def u32(re_p): return nx.peek32(re_to_nx(re_p))
def u16(re_p): return nx.peek16(re_to_nx(re_p))
def u8(re_p):  return nx.peek8(re_to_nx(re_p))
def read(re_p, size): return nx.read(re_to_nx(re_p), size)


def readRectHU(re_p):
    vtable, x1, y1, x2, y2 = struct.unpack('<Q8xII8xII', read(re_p, 0x28))
    assert nx_to_re(vtable) == 0x7103185ed0
    return (x1, y1, x2, y2)


def diff(a,b):
    for y,(rowA,rowB) in enumerate(zip(a,b)):
        for x,(itemA,itemB) in enumerate(zip(rowA,rowB)):
            if itemA != itemB:
                print(f'{x:3d},{y:3d} : {itemA} -> {itemB}')


if __name__ == '__main__':
    fs = FieldSystem.get()
    #print(fs.fields)
    field = fs.defaultField
    print(field)
    layers = field.itemLayers
    for x,y,tag in layers[0].tags.nonZeroTagIterator:
        print(f'{x},{y} {tag:8x}')

field = FieldSystem.get().defaultField
main = field.itemLayers
nx.resume()

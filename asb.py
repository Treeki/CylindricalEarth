from stream import *
from collections import namedtuple
import sys
import os

Root = namedtuple('Root', ('name','a','b','c','d','key','nodeIndex'))
Node = namedtuple('Node', ('type','za','zb','a','b','c','key'))
Tb1 = namedtuple('Tb1', ('name','a','b','c','d'))
Tb2 = namedtuple('Tb2', ('name','a','b','c','d','e'))
Tc = namedtuple('Tc', ('nameA', 'nameB', 'entries'))
Td = namedtuple('Td', ('type', 'dataOffset', 'key'))
Param = namedtuple('Param', ('name', 'default'))

class ASB:
    def __init__(self):
        self.name = None
        self.roots = []
        self.nodes = []
        self.thingB = []
        self.thingC = []
        self.thingD = []
        self.strParams = []
        self.intParams = []
        self.floatParams = []
        self.boolParams = []
        self.vecParams = []
        self.list58 = []

    def load(self, blob):
        stm = DataInputStream(blob, LITTLE_ENDIAN)
        assert(stm.read_bytes(4) == b'ASB ')
        assert(stm.read_u32() == 0x0407) # version
        nameOffsetInStringTable = stm.read_u32()
        rootCount = stm.read_u32()
        nodeCount = stm.read_u32()
        thingB_count = stm.read_u32()
        thingC_count = stm.read_u32()
        thingD_count = stm.read_u32()
        varTableOffset = stm.read_u32()
        stringTableOffset = stm.read_u32()
        offset28 = stm.read_u32()
        offset2C = stm.read_u32()
        thingB = stm.read_u32()
        thingC = stm.read_u32()
        thingD = stm.read_u32()
        thingE = stm.read_u32()
        thingF = stm.read_u32()
        count44 = stm.read_u32()
        offset48 = stm.read_u32()
        count48 = stm.read_u32()
        offset50 = stm.read_u32()
        offset54 = stm.read_u32()
        offset58 = stm.read_u32()
        u5C = stm.read_u32() #unused?
        u60 = stm.read_u32() #unused?
        u64 = stm.read_u32() #unused?
        assert(stm.pos == 0x68)

        def getStr(offset):
            return read_bytestring(stm.at(stringTableOffset + offset))

        self.name = getStr(nameOffsetInStringTable)
        #print(f'ZZ {rootCount:3d} {nodeCount:4d} {thingB_count:4d} {thingC_count} {thingD_count:3d} {varTableOffset:5x} {stringTableOffset:5x} {offset28:5x} {offset2C:5x} {thingB:5x} {thingC:5x} {thingD:5x} {thingE:5x} {thingF:5x} {count44:2d} {offset48:5x} {count48:2d} {offset50:5x} {offset54:5x} {offset58:5x} {u5C} {u60} {u64} {self.name}')
        print(f'ZZ r*{rootCount:3d} n*{nodeCount:4d} b:{thingB_count:4d} c*{thingC_count} d*{thingD_count:3d} v@{varTableOffset:5x} s@{stringTableOffset:5x} 28@{offset28:5x} 2C@{offset2C:5x} b@{thingB:5x} c@{thingC:5x} d@{thingD:5x} e@{thingE:5x} f@{thingF:5x} 44*{count44:2d} 48@{offset48:5x} 48*{count48:2d} 50@{offset50:5x} 54@{offset54:5x} 58@{offset58:5x} {u5C} {u60} {u64} {self.name}')
        #print(name)

        # roots
        for i in range(rootCount):
            name = getStr(stm.read_u32())
            a = stm.read_u32()
            b = stm.read_float() # some of the others might also be floats? must check
            c = stm.read_u32()
            d = stm.read_u32()
            key = stm.read_bytes(16)
            nodeIndex = stm.read_u16()
            assert(stm.read_u16() == 0) # padding?
            self.roots.append(Root(name, a, b, c, d, key.hex(), nodeIndex))

        for i in range(nodeCount):
            type = stm.read_u16()
            a = stm.read_u16()
            tableOffset = stm.read_u32()
            dataOffset = stm.read_u32()
            if tableOffset > 0:
                table = stm.at(tableOffset)
                stringList = []
                for i in range(table.read_u32()):
                    stringList.append(getStr(table.read_u32()))
            else:
                stringList = None
            b = stm.read_u32()
            c = stm.read_u32()
            key = stm.read_bytes(16)
            self.nodes.append(Node(type, stringList, dataOffset, a, b, c, key.hex()))

        # list 58
        stm.seek(offset58)
        for i in range(stm.read_u32()):
            self.list58.append(getStr(stm.read_u32()))

        # thingB
        stm.seek(thingB)
        for i in range(thingB_count):
            stmB = stm.at(stm.read_u32())

            count1 = stmB.read_u32()
            count2 = stmB.read_u32()
            t1, t2 = [], []
            for j in range(count1):
                name = getStr(stmB.read_u32())
                assert(stmB.read_u32() == 0) # placeholder filled in by the game
                a = stmB.read_u32()
                b = stmB.read_u32()
                c = stmB.read_u32()
                d = stmB.read_float()
                t1.append(Tb1(name, a, b, c, d))
            for j in range(count2):
                name = getStr(stmB.read_u32())
                assert(stmB.read_u32() == 0) # placeholder filled in by the game
                a = stmB.read_u32()
                b = stmB.read_u32()
                c = stmB.read_u32()
                d = stmB.read_float()
                e = stmB.read_float()
                t2.append(Tb2(name, a, b, c, d, e))
            self.thingB.append((t1, t2))

        # thingC
        stm.seek(thingC)
        for i in range(thingC_count):
            count = stm.read_u32()
            nameA = getStr(stm.read_u32())
            nameB = getStr(stm.read_u32())
            entries = []
            for j in range(count):
                subName = getStr(stm.read_u32())
                idA = stm.read_u16()
                idB = stm.read_u16()
                entries.append((subName, idA, idB))
            self.thingC.append(Tc(nameA, nameB, entries))

        # thingD
        stm.seek(thingD)
        for i in range(thingD_count):
            type = stm.read_u32()
            dataOffset = stm.read_u32()
            key = stm.read_bytes(16)
            self.thingD.append(Td(type, dataOffset, key))

        # variable table
        stm.seek(varTableOffset + 0x28)
        defaultBase = varTableOffset + 0x30 + 4 * (stm.read_u16() + stm.read_u16())
        stm.seek(varTableOffset)
        for i in range(5):
            count = stm.read_u16()
            offset = stm.read_u16()
            defaultOffset = stm.read_u16()
            assert(stm.read_u16() == 0)
            stmB = stm.at(varTableOffset + 0x30 + offset * 4)
            stmDef = stm.at(defaultBase + defaultOffset)
            for j in range(count):
                x = stmB.read_u32()
                assert (x & 0xFF000000) == 0
                name = getStr(x & 0xFFFFFFFF)
                if i == 0:
                    default = getStr(stmDef.read_u32())
                    self.strParams.append(Param(name, default))
                elif i == 1:
                    default = stmDef.read_u32()
                    self.intParams.append(Param(name, default))
                elif i == 2:
                    default = stmDef.read_float()
                    self.floatParams.append(Param(name, default))
                elif i == 3:
                    default = (stmDef.read_u32() != 0)
                    self.boolParams.append(Param(name, default))
                elif i == 4:
                    default = (stmDef.read_float(), stmDef.read_float(), stmDef.read_float())
                    self.vecParams.append(Param(name, default))

        for e in self.roots: print(e)
        for e in self.nodes: print(e)
        for e in self.list58: print(e)
        for i, (t1, t2) in enumerate(self.thingB):
            print(f'b group {i}')
            for e in t1: print(e)
            for e in t2: print(e)
        for e in self.thingC: print(e)
        for e in self.thingD: print(e)
        for e in self.strParams: print('str', e)
        for e in self.intParams: print('int', e)
        for e in self.floatParams: print('float', e)
        for e in self.boolParams: print('bool', e)
        for e in self.vecParams: print('vec', e)

        '''
        # offset 28
        stm.seek(offset28)
        count = stm.read_u32()
        for i in range(count):
            ptr = stm.read_u32()
            name1 = getStr(stm.read_u32())
            name2 = getStr(stm.read_u32())
            print(f'o28 {ptr:08x} {name1} {name2}')

        # var table
        stm.seek(varTableOffset)
        #table = stm.read_bytes(0x30)
        #print(table.hex(' '))
        for i in range(6):
            count = stm.read_u16()
            offset = stm.read_u16()
            offset2 = stm.read_u16()
            assert(stm.read_u16() == 0)
            print(f'group:{i} offset:{offset} offset2:{offset2} count:{count}')
            stmB = stm.at(varTableOffset + 0x30 + offset * 4)
            for j in range(count):
                x = stmB.read_u32()
                assert (x & 0xFF000000) == 0
                name = getStr(x & 0xFFFFFFFF)
                print(name)
        '''


        print(f'{stm.covered_bytes} / {stm.length} bytes read')


if __name__ == '__main__':
    for path in sys.argv[1:]:
        # bad version numbers in some...
        if path.endswith('ObjectAirConditioner.root.asb'):
            continue
        if path.endswith('ResolvedByHelper.root.asb'):
            continue
        # print(path)
        with open(path, 'rb') as f:
            asb = ASB()
            asb.load(f.read())



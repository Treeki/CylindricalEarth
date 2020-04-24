# Based off: https://github.com/mdbell/Noexes/blob/master/client/src/me/mdbell/noexs/core/Debugger.java

import socket
import struct
import enum

Status = enum.IntEnum('Status', ('STOPPED', 'RUNNING', 'PAUSED'), start=0)

Command = enum.IntEnum('Command', (
    'STATUS', 'POKE8', 'POKE16', 'POKE32', 'POKE64',
    'READ', 'WRITE', 'CONTINUE', 'PAUSE',
    'ATTACH', 'DETACH', 'QUERY_MEMORY', 'QUERY_MEMORY_MULTI',
    'CURRENT_PID', 'GET_ATTACHED_PID', 'GET_PIDS', 'GET_TITLEID',
    'DISCONNECT', 'READ_MULTI', 'SET_BREAKPOINT'))

MemoryType = enum.IntEnum('MemoryType', (
    'UNMAPPED', 'IO', 'NORMAL', 'CODE_STATIC', 'CODE_MUTABLE',
    'HEAP', 'SHARED', 'WEIRD_MAPPED', 'MODULE_CODE_STATIC', 'MODULE_CODE_MUTABLE',
    'IPC_BUFFER_0', 'MAPPED', 'THREAD_LOCAL', 'ISOLATED_TRANSFER', 'TRANSFER',
    'PROCESS', 'RESERVED', 'IPC_BUFFER_1', 'IPC_BUFFER_3', 'KERNEL_STACK',
    'CODE_READ_ONLY', 'CODE_WRITABLE'
), start=0)

class NoexsClient:
    def __init__(self, address):
        self.sock = socket.create_connection(address)

    def _recvall(self, amount):
        buf = b''
        while len(buf) < amount:
            buf += self.sock.recv(amount - len(buf))
        return buf

    def _recv_result(self):
        value = struct.unpack('<I', self._recvall(4))[0]
        mod = value & 0x1FF
        desc = (value >> 9) & 0x1FFF
        return (mod, desc)

    def _recv_compressed(self):
        flag, dlen = struct.unpack('<BI', self._recvall(5))
        if flag == 0:
            return self._recvall(dlen)
        else:
            outdata = bytearray(dlen)
            indata = self._recvall(struct.unpack('<I', self._recvall(4))[0])
            pos = 0
            for i in range(0, len(indata), 2):
                for j in range(indata[i + 1]):
                    outdata[pos + j] = indata[i]
                pos += indata[i + 1]
            return bytes(outdata)

    def _assert_result_ok(self, throwaway=False):
        result = self._recv_result()
        if result != (0,0):
            if throwaway:
                self._recv_result()
            raise ValueError('connection error %d,%d' % result)

    def get_status(self):
        self.sock.sendall(struct.pack('<B', int(Command.STATUS)))
        status, major, minor, patch = struct.unpack('<BBBB', self._recvall(4))
        self._assert_result_ok()
        return (Status(status), major, minor, patch)

    def poke8(self, addr, value):
        self.sock.sendall(struct.pack('<BQB', int(Command.POKE8), addr, value))
        self._assert_result_ok()
    def poke16(self, addr, value):
        self.sock.sendall(struct.pack('<BQH', int(Command.POKE16), addr, value))
        self._assert_result_ok()
    def poke32(self, addr, value):
        self.sock.sendall(struct.pack('<BQI', int(Command.POKE32), addr, value))
        self._assert_result_ok()
    def poke64(self, addr, value):
        self.sock.sendall(struct.pack('<BQQ', int(Command.POKE64), addr, value))
        self._assert_result_ok()
    def peek8(self, addr):
        return struct.unpack('<B', self.read(addr, 1))[0]
    def peek16(self, addr):
        return struct.unpack('<H', self.read(addr, 2))[0]
    def peek32(self, addr):
        return struct.unpack('<I', self.read(addr, 4))[0]
    def peek64(self, addr):
        return struct.unpack('<Q', self.read(addr, 8))[0]

    def read(self, addr, size):
        self.sock.sendall(struct.pack('<BQI', int(Command.READ), addr, size))
        self._assert_result_ok(throwaway=True)

        pos = 0
        result = b''
        while len(result) < size:
            self._assert_result_ok(throwaway=True)
            result += self._recv_compressed()
        self._recv_result() #ignored
        return result

    def write(self, addr, data):
        self.sock.sendall(struct.pack('<BQI', int(Command.WRITE), addr, len(data)))
        self._assert_result_ok(throwaway=True)

        self.sock.sendall(data)
        self._assert_result_ok()

    def resume(self):
        self.sock.sendall(struct.pack('<B', int(Command.CONTINUE)))
        self._assert_result_ok()

    def pause(self):
        self.sock.sendall(struct.pack('<B', int(Command.PAUSE)))
        self._assert_result_ok()

    def attach(self, pid):
        self.sock.sendall(struct.pack('<BQ', int(Command.ATTACH), pid))
        self._assert_result_ok()

    def detach(self):
        self.sock.sendall(struct.pack('<B', int(Command.DETACH)))
        self._assert_result_ok()

    def set_breakpoint(self, id, addr, flags):
        self.sock.sendall(struct.pack('<BIQQ', int(Command.SET_BREAKPOINT), id, addr, flags))
        self._assert_result_ok()

    def set_watchpoint(self, id, addr, flags):
        raise NotImplementedError

    def get_pids(self):
        self.sock.sendall(struct.pack('<B', int(Command.GET_PIDS)))
        count = struct.unpack('<I', self._recvall(4))[0]
        if count > 0:
            pids = list(struct.unpack('<%dQ' % count, self._recvall(8 * count)))
        else:
            pids = []
        self._assert_result_ok()
        return pids

    def get_title_id(self, pid):
        self.sock.sendall(struct.pack('<BQ', int(Command.GET_TITLEID), pid))
        tid = struct.unpack('<Q', self._recvall(8))[0]
        self._assert_result_ok()
        return tid

    def get_memory_info(self, start=0, max=10000):
        self.sock.sendall(struct.pack('<BQI', int(Command.QUERY_MEMORY_MULTI), start, max))
        results = []
        for i in range(max):
            addr, size, typ, perm = struct.unpack('<QQII', self._recvall(24))
            typ = MemoryType(typ)
            self._assert_result_ok()
            if typ == MemoryType.RESERVED:
                break
            else:
                results.append((addr, size, typ, perm))
        self._recv_result() #ignored
        return results


from pynoexs import *

def find_ACNH(nx):
    for pid in reversed(nx.get_pids()):
        if nx.get_title_id(pid) == 0x1006f8002326000:
            return pid
    return None

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
def u32(re_p): return nx.peek32(re_to_nx(re_p))
def u16(re_p): return nx.peek16(re_to_nx(re_p))
def u8(re_p):  return nx.peek8(re_to_nx(re_p))
def read(re_p, size): return nx.read(re_to_nx(re_p), size)

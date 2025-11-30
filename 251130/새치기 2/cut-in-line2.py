N, M, Q = map(int, input().split())
names = input().split()

command = []
a = []
b = []
c = []

for _ in range(Q):
    line = input().split()
    cmd = int(line[0])
    command.append(cmd)

    if cmd == 1:
        a.append(line[1])
        b.append(line[2])
        c.append("")
    elif cmd == 2:
        a.append(line[1])
        b.append("")
        c.append("")
    else:
        a.append(line[1])
        b.append(line[2])
        c.append(line[3])

# Please write your code here.
name_to_id = {names[i]: i for i in range(N)}

prev = [-1] * N
nxt = [-1] * N

head = [-1] * (M + 1)
tail = [-1] * (M + 1)

line_of = [0] * N

X = N // M  
for line_idx in range(M):  
    ln = line_idx + 1      
    start = line_idx * X
    end = (line_idx + 1) * X - 1

    head[ln] = start
    tail[ln] = end

    for i in range(start, end + 1):
        line_of[i] = ln
        if i > start:
            prev[i] = i - 1
        else:
            prev[i] = -1
        if i < end:
            nxt[i] = i + 1
        else:
            nxt[i] = -1

def detach_single(pid):
    ln = line_of[pid]
    if ln == 0:
        return  

    p = prev[pid]
    n = nxt[pid]

    if p != -1:
        nxt[p] = n
    else:
        head[ln] = n

    if n != -1:
        prev[n] = p
    else:
        tail[ln] = p

    prev[pid] = -1
    nxt[pid] = -1
    line_of[pid] = 0

def detach_block(a_id, b_id):
    ln = line_of[a_id]
    pa = prev[a_id]
    nb = nxt[b_id]

    if pa != -1:
        nxt[pa] = nb
    else:
        head[ln] = nb

    if nb != -1:
        prev[nb] = pa
    else:
        tail[ln] = pa

    prev[a_id] = -1
    nxt[b_id] = -1

for qi in range(Q):
    cmd = command[qi]

    if cmd == 1:
        name_a = a[qi]
        name_b = b[qi]
        ida = name_to_id[name_a]
        idb = name_to_id[name_b]

        detach_single(ida)

        ln_b = line_of[idb]
        pb = prev[idb]

        if pb != -1:
            nxt[pb] = ida
        else:
            head[ln_b] = ida

        prev[ida] = pb
        nxt[ida] = idb
        prev[idb] = ida
        line_of[ida] = ln_b

    elif cmd == 2:
        name_a = a[qi]
        ida = name_to_id[name_a]
        detach_single(ida)

    else:
        name_a = a[qi]
        name_b = b[qi]
        name_c = c[qi]

        ida = name_to_id[name_a]
        idb = name_to_id[name_b]
        idc = name_to_id[name_c]

        detach_block(ida, idb)

        ln_c = line_of[idc]
        pc = prev[idc]

        if pc != -1:
            nxt[pc] = ida
        else:
            head[ln_c] = ida

        prev[ida] = pc
        nxt[idb] = idc
        prev[idc] = idb

        cur = ida
        while True:
            line_of[cur] = ln_c
            if cur == idb:
                break
            cur = nxt[cur]

for ln in range(1, M + 1):
    h = head[ln]
    if h == -1:
        print(-1)
    else:
        res = []
        cur = h
        while cur != -1:
            res.append(names[cur])
            cur = nxt[cur]
        print(" ".join(res))
N, M, Q = map(int, input().split())

line = [[0] * 100000 for _ in range(10)]
line_size = [0] * 10
cmd = [[0] * 4 for _ in range(10000)]

for i in range(M):
    nums = list(map(int, input().split()))
    if nums[0] == -1:
        line_size[i] = 0
        continue
    line_size[i] = nums[0]
    for j in range(nums[0]):
        line[i][j] = nums[j + 1]

for i in range(Q):
    query = list(map(int, input().split()))
    cmd[i][0] = query[0]
    if query[0] == 1:
        cmd[i][1] = query[1]
        cmd[i][2] = query[2]
    elif query[0] == 2:
        cmd[i][1] = query[1]
    elif query[0] == 3:
        cmd[i][1] = query[1]
        cmd[i][2] = query[2]
        cmd[i][3] = query[3]

# Please write your code here.
prev = [0] * (N + 1)
next = [0] * (N + 1)
line_of = [0] * (N + 1)

head = [0] * (M + 1)
tail = [0] * (M + 1)

for li in range(M): 
    sz = line_size[li]
    if sz == 0:
        continue

    people = line[li][:sz]
    ln = li + 1  

    head[ln] = people[0]
    tail[ln] = people[-1]

    for idx, p in enumerate(people):
        line_of[p] = ln
        if idx > 0:
            prev[p] = people[idx - 1]
            next[people[idx - 1]] = p

for qi in range(Q):
    t = cmd[qi][0]

    if t == 1:
        a = cmd[qi][1]
        b = cmd[qi][2]

        if line_of[a] == 0:
            continue 

        la = line_of[a]
        lb = line_of[b]

        pa = prev[a]
        na = next[a]

        if pa != 0:
            next[pa] = na
        else:
            head[la] = na

        if na != 0:
            prev[na] = pa
        else:
            tail[la] = pa

        prev[a] = 0
        next[a] = 0
        line_of[a] = 0 

        pb = prev[b]

        if pb != 0:
            next[pb] = a
        else:
            head[lb] = a

        prev[a] = pb
        next[a] = b
        prev[b] = a

        line_of[a] = lb

    elif t == 2:
        a = cmd[qi][1]

        if line_of[a] == 0:
            continue

        la = line_of[a]
        pa = prev[a]
        na = next[a]

        if pa != 0:
            next[pa] = na
        else:
            head[la] = na

        if na != 0:
            prev[na] = pa
        else:
            tail[la] = pa

        prev[a] = 0
        next[a] = 0
        line_of[a] = 0

    elif t == 3:
        a = cmd[qi][1]
        b = cmd[qi][2]
        c = cmd[qi][3]

        if line_of[a] == 0 or line_of[b] == 0:
            continue

        la = line_of[a]
        lb = line_of[b]

        pa = prev[a]
        nb = next[b]

        if pa != 0:
            next[pa] = nb
        else:
            head[la] = nb

        if nb != 0:
            prev[nb] = pa
        else:
            tail[la] = pa

        prev[a] = 0
        next[b] = 0

        lc = line_of[c]
        pc = prev[c]

        if pc != 0:
            next[pc] = a
        else:
            head[lc] = a
        prev[a] = pc

        prev[c] = b
        next[b] = c

        cur = a
        while True:
            line_of[cur] = lc
            if cur == b:
                break
            cur = next[cur]

for ln in range(1, M + 1):
    h = head[ln]
    if h == 0:
        print(-1)
    else:
        res = []
        cur = h
        while cur != 0:
            res.append(str(cur))
            cur = next[cur]
        print(" ".join(res))
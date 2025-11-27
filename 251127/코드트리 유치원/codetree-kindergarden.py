Q = int(input())

option = []
a = []
b = []

for _ in range(Q):
    query = list(map(int, input().split()))
    option.append(query[0])
    if query[0] == 1 or query[0] == 2:
        a.append(query[1])
        b.append(query[2])
    else:
        a.append(query[1])
        b.append(0)

# Please write your code here.
total_new = sum(b)
max_students = 1 + total_new

prev = [0] * (max_students + 1)
next = [0] * (max_students + 1)

cur_max = 1
head = 1
tail = 1
prev[1] = 0
next[1] = 0

out = []

for qi in range(Q):
    t = option[qi]
    ai = a[qi]
    bi = b[qi]

    if t == 1:
        if bi <= 0:
            continue

        s = cur_max + 1               
        e = cur_max + bi              
        cur_max = e

        for id in range(s, e + 1):
            prev[id] = id - 1 if id > s else 0
            next[id] = id + 1 if id < e else 0

        after = next[ai]                  

        next[ai] = s
        prev[s] = ai

        if after != 0:
            prev[after] = e
            next[e] = after
        else:
            tail = e

    elif t == 2:
        if bi <= 0:
            continue

        s = cur_max + 1
        e = cur_max + bi
        cur_max = e

        for id in range(s, e + 1):
            prev[id] = id - 1 if id > s else 0
            next[id] = id + 1 if id < e else 0

        before = prev[ai]                 

        if before != 0:
            next[before] = s
        else:
            head = s
        prev[s] = before

        next[e] = ai
        prev[ai] = e
    else:
        left = prev[ai]
        right = next[ai]

        if left == 0 and right == 0:
            out.append("-1")
            continue
        else:
            out_left = left
            out_right = right

        out.append(f"{out_left} {out_right}")

print("\n".join(out))
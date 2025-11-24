N, K = map(int, input().split())
Q = int(input())
type_arr = []
i_arr = []
j_arr = []
for _ in range(Q):
    t, x, y = map(int, input().split())
    type_arr.append(t)
    i_arr.append(x)
    j_arr.append(y)

# Please write your code here.
prev, nxt = [0] * (N + 1), [0] * (N + 1)
head, tail, size = [0] * (K + 1), [0] * (K + 1), [0] * (K + 1)

if N > 0:
    head[1] = 1
    tail[1] = N
    size[1] = N

    for x in range(1, N + 1):
        if x > 1:
            prev[x] = x - 1
        if x < N:
            nxt[x] = x + 1

for t_num, i_num, j_num in zip(type_arr, i_arr, j_arr):
    if t_num == 1:
        if size[i_num] == 0:
            continue
        
        book = head[i_num]

        new_head = nxt[book]
        head[i_num] = new_head
        if new_head != 0:
            prev[new_head] = 0
        else:
            tail[i_num] = 0

        nxt[book] = 0
        prev[book] = 0
        size[i_num] -= 1

        if size[j_num] == 0:
            head[j_num] = tail[j_num] = book
        else:
            old_tail = tail[j_num]
            nxt[old_tail] = book
            prev[book] = old_tail
            tail[j_num] = book
        size[j_num] += 1
    elif t_num == 2:
        if size[i_num] == 0:
            continue

        book = tail[i_num]

        new_tail = prev[book]
        tail[i_num] = new_tail
        if new_tail != 0:
            nxt[new_tail] = 0
        else:
            head[i_num] = 0

        prev[book] = 0
        nxt[book] = 0
        size[i_num] -= 1

        if size[j_num] == 0:
            head[j_num] = tail[j_num] = book
        else:
            old_head = head[j_num]
            prev[old_head] = book
            nxt[book] = old_head
            head[j_num] = book
        size[j_num] += 1
    elif t_num == 3:
        if i_num == j_num or size[i_num] == 0:
            continue

        hi, ti = head[i_num], tail[i_num]
        hj, tj = head[j_num], tail[j_num]

        if size[j_num] == 0:
            head[j_num],tail[j_num] = hi, ti
        else:
            prev[hj] = ti
            nxt[ti] = hj
            head[j_num] = hi

        head[i_num] = tail[j_num] = 0
        size[j_num] += size[i_num]
        size[i_num] = 0
    elif t_num == 4:
        if i_num == j_num or size[i_num] == 0:
            continue

        hi, ti = head[i_num], tail[i_num]
        hj, tj = head[j_num], tail[j_num]

        if size[j_num] == 0:
            head[j_num], tail[j_num] = hi, ti
        else:
            nxt[tj] = hi
            prev[hi] = tj
            tail[j_num] = ti

        head[i_num] = tail[i_num] = 0
        size[j_num] += size[i_num]
        size[i_num] = 0

out_lines = []
for shelf in range(1, K + 1):
    cnt = size[shelf]
    if cnt == 0:
        out_lines.append("0")
    else:
        books = []
        cur = head[shelf]
        while cur != 0:
            books.append(str(cur))
            cur = nxt[cur]
        out_lines.append(str(cnt) + " " + " ".join(books))

print("\n".join(out_lines))
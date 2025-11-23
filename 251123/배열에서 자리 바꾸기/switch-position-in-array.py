N = int(input())
Q = int(input())
queries = [tuple(map(int, input().split())) for _ in range(Q)]
a, b, c, d = zip(*queries)
a, b, c, d = list(a), list(b), list(c), list(d)

# Please write your code here.
prev = [0] * (N + 1)
next = [0] * (N + 1)

for i in range(1, N + 1):
    if i > 1:
        prev[i] = i - 1
    if i < N:
        next[i] = i + 1

head = 1 

def swap_segments(a, b, c, d):
    global head, prev, next

    ap, bn = prev[a], next[b]
    cp, dn = prev[c], next[d]

    if bn == c and cp == b:
        if ap != 0:
            next[ap] = c
        else:
            head = c
        prev[c] = ap

        next[d] = a
        prev[a] = d

        next[b] = dn
        if dn != 0:
            prev[dn] = b

    elif dn == a and ap == d:
        if cp != 0:
            next[cp] = a
        else:
            head = a
        prev[a] = cp

        next[b] = c
        prev[c] = b

        next[d] = bn
        if bn != 0:
            prev[bn] = d
    else:
        if ap != 0:
            next[ap] = bn
        else:
            head = bn
        if bn != 0:
            prev[bn] = ap

        if cp != 0:
            next[cp] = dn
        else:
            head = dn
        if dn != 0:
            prev[dn] = cp

        if ap != 0:
            next[ap] = c
        else:
            head = c
        prev[c] = ap

        if bn != 0:
            prev[bn] = d
        next[d] = bn

        if cp != 0:
            next[cp] = a
        else:
            head = a
        prev[a] = cp

        if dn != 0:
            prev[dn] = b
        next[b] = dn


for i in range(Q):
    swap_segments(a[i], b[i], c[i], d[i])

res = []
cur = head
while cur != 0:
    res.append(str(cur))
    cur = next[cur]

print(" ".join(res))
n = int(input())
s = [input() for _ in range(n)]

# Please write your code here.
from functools import cmp_to_key

info = []

for st in s:
    open_cnt, close_cnt = 0, 0
    internal = 0
    for ch in st:
        if ch == '(':
            open_cnt += 1
        else:
            close_cnt += 1
            internal += open_cnt
    info.append((open_cnt, close_cnt, internal))

def cmp(a, b):
    oa, ca, _ = a
    ob, cb, _ = b
    left = oa * cb
    right = ob * ca

    if left > right:
        return -1
    if left < right:
        return 1

    return 0

info.sort(key = cmp_to_key(cmp))

total_opens = 0
ans = 0

for o, c, internal in info:
    ans += internal
    ans += total_opens * c
    total_opens += o

print(ans)
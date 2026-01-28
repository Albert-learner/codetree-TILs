A = input()
B = input()
del_order = list(map(int, input().split()))

# Please write your code here.
import sys

n, m = len(A), len(B)

del_time = [0] * n
for step, pos in enumerate(del_order, 1):
    del_time[pos - 1] = step

def ok(t: int) -> bool:
    j = 0
    for i, ch in enumerate(A):
        if del_time[i] > t:
            if ch == B[j]:
                j += 1
                if j == m:
                    return True

    return False

if not ok(0):
    print(0)
    sys.exit(0)

lo, hi = 0, n
while lo + 1 < hi:
    mid = (lo + hi) // 2
    if ok(mid):
        lo = mid
    else:
        hi = mid

print(lo + 1)
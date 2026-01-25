n, k = map(int, input().split())
x = [int(input()) for _ in range(n)]

# Please write your code here.
x.sort()

def can_cover(R: int) -> bool:
    cnts, i = 0, 0
    while i < n:
        cnts += 1
        if cnts > k:
            return False

        reach = x[i] + 2 * R
        while i < n and x[i] <= reach:
            i += 1

    return True

lo, hi = 0, 10 ** 9
while lo < hi:
    mid = (lo + hi) // 2
    if can_cover(mid):
        hi = mid
    else:
        lo = mid + 1

print(lo)
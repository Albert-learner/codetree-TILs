N, M, C = map(int, input().split())
t = list(map(int, input().split()))

# Please write your code here.
t.sort()

def can(max_wait: int) -> bool:
    i, buses = 0, 0
    while i < N:
        buses += 1
        if buses > M:
            return False

        first_time = t[i]
        cnts = 0

        while i < N and cnts < C and t[i] - first_time <= max_wait:
            i += 1
            cnts += 1

    return True

lo, hi = 0, 10 ** 9
while lo < hi:
    mid = (lo + hi) // 2
    if can(mid):
        hi = mid
    else:
        lo = mid + 1

print(lo)
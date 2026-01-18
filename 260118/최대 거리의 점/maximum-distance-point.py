n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
arr.sort()

def can_place(d: int) -> int:
    cnts = 1
    last = arr[0]

    for i in range(1, n):
        if arr[i] - last >= d:
            cnts += 1
            last = arr[i]
            if cnts >= m:
                return True

    return cnts >= m

lo, hi = 0, arr[-1] - arr[0]
ans = 0

while lo <= hi:
    mid = (lo + hi) // 2
    if can_place(mid):
        ans = mid
        lo = mid + 1
    else:
        hi = mid - 1

print(ans)
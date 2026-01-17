n = int(input())
k = int(input())

# Please write your code here.
def count_leq(x: int) -> int:
    cnts = 0
    for i in range(1, n + 1):
        cnts += min(n, x // i)

    return cnts

left, right = 1, n * n
ans = right

while left <= right:
    mid = (left + right) // 2
    if count_leq(mid) >= k:
        ans = mid
        right = mid - 1
    else:
        left = mid + 1

print(ans)
n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
def can_make(k: int) -> bool:
    cnts = 0
    for x in arr:
        cnts += x // k
        if cnts >= m:
            return True
    
    return False

left, right = 1, max(arr)
ans = 0

while left <= right:
    mid = (left + right) // 2
    if can_make(mid):
        ans = mid
        left = mid + 1
    else:
        right = mid - 1

print(ans)
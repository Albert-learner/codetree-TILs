n, m = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
while m > 0:
    max_cst, max_cst_idx = max(arr), arr.index(max(arr))
    arr[max_cst_idx] -= 1

    m -= 1

print(max(arr))
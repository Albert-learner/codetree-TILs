n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [int(input()) for _ in range(m)]

# Please write your code here.
for qry in queries:
    idx = -1
    left, right = 0, n - 1

    while left <= right:
        if qry not in arr:
            break

        mid = (left + right) // 2
        if arr[mid] == qry:
            idx = mid + 1
            break

        if arr[mid] > qry:
            right = mid - 1
        else:
            left = mid + 1

    print(idx)
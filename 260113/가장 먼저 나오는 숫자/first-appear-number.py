n, m = map(int, input().split())
arr = list(map(int, input().split()))
query = list(map(int, input().split()))

# Please write your code here.
def binary_search(target):
    left, right = 0, n - 1
    idx = n

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            idx = min(idx, mid)

        if arr[mid] >= target:
            right = mid - 1
        else:
            left = mid + 1

    return idx

for qry in query:
    idx = binary_search(qry)
    print(idx + 1 if idx != n else -1)
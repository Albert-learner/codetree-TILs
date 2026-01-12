n, m = map(int, input().split())
points = list(map(int, input().split()))
segments = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
def binary_search(start, end, target):
    if target > end or target < start:
        return 0
    else:
        while start <= end:
            mid = (start + end) // 2
            if mid == target:
                return 1
            elif mid > target:
                end = mid - 1
            else:
                start = mid + 1
        
        return 0

for x, y in segments:
    cnts = 0
    for point in points:
        cnts += binary_search(x, y, point)
    print(cnts)

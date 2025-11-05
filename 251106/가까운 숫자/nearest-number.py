from sortedcontainers import SortedList

n = int(input())
queries = list(map(int, input().split()))

points = SortedList([0])   
gaps = SortedList()        
for x in queries:
    idx = points.bisect_left(x)

    left_exists = (idx > 0)
    right_exists = (idx < len(points))

    if left_exists and right_exists:
        p = points[idx - 1]
        s = points[idx]

        gaps.remove(s - p)       
        gaps.add(x - p)
        gaps.add(s - x)
    elif left_exists:
        p = points[idx - 1]
        gaps.add(x - p)
    elif right_exists:
        s = points[idx]
        gaps.add(s - x)

    points.add(x)

    print(gaps[0] if gaps else 0)

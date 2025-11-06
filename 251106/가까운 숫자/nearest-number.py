n = int(input())
queries = list(map(int, input().split()))

# Please write your code here.
from sortedcontainers import SortedList

points = SortedList([0])      
gaps = SortedList()           
for x in queries:
    i = points.bisect_left(x)

    if i > 0:
        left = points[i-1]
        gaps.add(x - left)
    if i < len(points):
        right = points[i]
        gaps.add(right - x)


    if 0 < i < len(points):
        gaps.remove(right - left) 

    points.add(x)

    print(gaps[0])
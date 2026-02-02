n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
import heapq

if n <= 1:
    print(0)
else:
    heapq.heapify(arr)
    total = 0

    while len(arr) > 1:
        a = heapq.heappop(arr)
        b = heapq.heappop(arr)
        s = a + b
        total += s
        heapq.heappush(arr, s)

    print(total)
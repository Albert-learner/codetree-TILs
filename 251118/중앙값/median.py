import heapq

t = int(input())
for _ in range(t):
    m = int(input())
    arr = list(map(int, input().split()))

    # Please write your code here.
    left = []   
    right = []  

    medians = []

    for i, x in enumerate(arr, 1):
        if not left or x <= -left[0]:
            heapq.heappush(left, -x)
        else:
            heapq.heappush(right, x)

        if len(left) > len(right) + 1:
            val = -heapq.heappop(left)
            heapq.heappush(right, val)
        elif len(right) > len(left):
            val = heapq.heappop(right)
            heapq.heappush(left, -val)

        if i % 2 == 1:
            medians.append(-left[0])

    print(*medians)
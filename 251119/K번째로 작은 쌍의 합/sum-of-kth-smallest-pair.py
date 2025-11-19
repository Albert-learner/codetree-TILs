n, m, k = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

# Please write your code here.
import heapq

arr1.sort()
arr2.sort()
limit = min(n, k)
pq = []

for i in range(limit):
    heapq.heappush(pq, (arr1[i] + arr2[0], i, 0))

cnt = 0
ans = 0

while pq and cnt < k:
    s, i, j = heapq.heappop(pq)
    ans = s
    cnt += 1

    if j + 1 < m:
        heapq.heappush(pq, (arr1[i] + arr2[j + 1], i, j + 1))

print(ans)
n, m, k = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

# Please write your code here.
import heapq

pq = []
for ar1_el in arr1:
    for ar2_el in arr2:
        heapq.heappush(pq, (ar1_el + ar2_el, ar1_el, ar2_el))

print(pq[k - 1][0])
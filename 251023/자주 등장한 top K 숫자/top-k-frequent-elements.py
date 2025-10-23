n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
import heapq as hq
from collections import Counter

arr_cntr = Counter(arr)
top_k = hq.nlargest(k, arr_cntr.items(), key = lambda x: (x[1], x[0]))

for num, _ in top_k:
    print(num, end = ' ')

n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [int(input()) for _ in range(m)]

# Please write your code here.
from collections import Counter

arr_cntr = Counter(arr)
for qry in queries:
    if qry in arr_cntr:
        print(arr_cntr[qry])
    else:
        print(0)
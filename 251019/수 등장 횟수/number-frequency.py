n, m = map(int, input().split())
arr = list(map(int, input().split()))
nums = list(map(int, input().split()))

# Please write your code here.
from collections import Counter

arr_cntr = Counter(arr)
for num in nums:
    if num in arr_cntr.keys():
        print(arr_cntr[num], end = ' ')
    else:
        print(0, end = ' ')
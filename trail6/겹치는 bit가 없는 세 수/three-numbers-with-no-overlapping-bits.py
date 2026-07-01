n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
from itertools import combinations

max_cst = 0
for a, b, c in combinations(arr, 3):
    if (a & b) == 0 and (b & c) == 0 and (a & c) == 0:
        max_cst = max(max_cst, a + b + c)

print(max_cst)
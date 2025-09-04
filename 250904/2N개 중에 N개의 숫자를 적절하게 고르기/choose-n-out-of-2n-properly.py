n = int(input())
num = list(map(int, input().split()))

# Please write your code here.
from itertools import combinations

total = sum(num)

min_sum_diff = min(abs(total - 2 * sum(comb)) for comb in combinations(num, n))
print(min_sum_diff)
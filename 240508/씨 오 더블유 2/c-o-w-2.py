from collections import Counter
from functools import reduce

N = int(input())
n_str = input()

n_str_cntr = Counter(n_str)
print(reduce(lambda x, y: x * y, n_str_cntr.values()))
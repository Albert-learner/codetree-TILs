n = int(input())
words = [input() for _ in range(n)]

# Please write your code here.
from collections import Counter

words_sort_set = [tuple(sorted(set(word))) for word in words]
words_sort_set_cntr = Counter(words_sort_set)

print(max(words_sort_set_cntr.values()))

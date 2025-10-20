n = int(input())
words = [input() for _ in range(n)]

# Please write your code here.
from collections import Counter

words_cntr = Counter(words)
print(max(words_cntr.values()))

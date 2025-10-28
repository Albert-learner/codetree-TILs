n = int(input())
words = [input() for _ in range(n)]

# Please write your code here.
from collections import Counter

words_cntr = sorted(list(Counter(words).items()))
for word, cnts in words_cntr:
    print(word, cnts)
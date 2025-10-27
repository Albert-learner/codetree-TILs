n = int(input())
words = [input() for _ in range(n)]

# Please write your code here.
from collections import Counter

words_cntr_lst = sorted(list(Counter(words).items()), key = lambda x:x[0])
words_total_cnts = sum(list(zip(*words_cntr_lst))[1])
words_ratios = []
for word, cnts in words_cntr_lst:
    ratio = (cnts / words_total_cnts) * 100
    words_ratios.append((word, ratio))

for word, ratio in words_ratios:
    print("{} {:.4f}".format(word, ratio))
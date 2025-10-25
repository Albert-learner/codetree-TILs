n = int(input())
words = [input() for _ in range(n)]

# Please write your code here.
from collections import Counter

keys = ("".join(sorted(w)) for w in words)

cnt = Counter(keys)

print(max(cnt.values()) if cnt else 0)
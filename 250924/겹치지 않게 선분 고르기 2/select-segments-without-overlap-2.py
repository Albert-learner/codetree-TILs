n = int(input())
x1, x2 = [], []
for _ in range(n):
    a, b = map(int, input().split())
    x1.append(a)
    x2.append(b)

# Please write your code here.
segs = sorted(zip(x1, x2), key = lambda p: (p[1], p[0]))

cnts = 0
last_end = -10 ** 9
for s, e in segs:
    if s > last_end:
        cnts += 1
        last_end = e

print(cnts)
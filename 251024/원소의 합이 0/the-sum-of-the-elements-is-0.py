n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
D = list(map(int, input().split()))

# Please write your code here.
from bisect import bisect_left, bisect_right

AB = [a + b for a in A for b in B]
CD = [c + d for c in C for d in D]

AB.sort()
CD.sort()

count = 0
for s in AB:
    target = -s
    left = bisect_left(CD, target)
    right = bisect_right(CD, target)
    count += (right - left)

print(count)
n, m = map(int, input().split())
queries = list(map(int, input().split()))

# Please write your code here.
from sortedcontainers import SortedSet

balls = SortedSet([i for i in range(1, m + 1)])
for r_ball in queries:
    balls.remove(r_ball)
    print(balls[-1])
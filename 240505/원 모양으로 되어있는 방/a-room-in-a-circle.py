from collections import deque
import sys

N = int(input())
people = deque([int(input()) for _ in range(N)])

min_dists = sys.maxsize
for i in range(N):
    people.rotate(1)
    min_dist = 0
    for i in range(1, N):
        min_dist += people[i] * i

    min_dists = min(min_dists, min_dist)

print(min_dists)
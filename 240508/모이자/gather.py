import sys

N = int(input())
people = list(map(int, input().split()))

min_dists = sys.maxsize
for i in range(N):
    dists = 0
    for j in range(N):
        if i == j:
            continue

        dists += abs(j - i) * people[j]

    min_dists = min(min_dists, dists)

print(min_dists)
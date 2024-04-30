import sys

N = int(input())
A_people = list(map(int, input().split()))
B_people = list(map(int, input().split()))

min_dists = 0
for i in range(N):
    if A_people[i] > B_people[i]:
        dists = A_people[i] - B_people[i]
        A_people[i] -= dists
        A_people[i + 1] += dists
        min_dists += dists

print(min_dists)
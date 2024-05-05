import sys

N = int(input())
chkpoints = [tuple(map(int, input().split())) for _ in range(N)]

min_dists = sys.maxsize
excludes = []
for i in range(1, N - 1):
    excludes.append(chkpoints[:i] + chkpoints[i + 1:])

for exclude in excludes:
    x_lst, y_lst = list(list(zip(*exclude))[0]), list(list(zip(*exclude))[1])
    min_dist = 0
    for i in range(len(x_lst) - 1):
        min_dist += abs(x_lst[i + 1] - x_lst[i])
    
    for i in range(len(y_lst) - 1):
        min_dist += abs(y_lst[i + 1] - y_lst[i])

    min_dists = min(min_dists, min_dist)

print(min_dists)
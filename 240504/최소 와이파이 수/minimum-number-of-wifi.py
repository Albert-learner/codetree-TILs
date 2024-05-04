N, M = map(int, input().split())
people = list(map(int, input().split()))

def new_idx(x, n_idx):
    for i in range(N):
        if i >= n_idx and people[i] == 1:
            return i
        elif i == N - 1:
            return n_idx
        else:
            continue

def is_range(x):
    if x >= N:
        return False
    elif people[x] == 0:
        return True
    else:
        return False

cnts = 0
if 1 not in people:
    print(cnts)
else:
    idx = 0
    while idx < N:
        if people[idx: idx + 2 * M + 1].count(1) != 0:
            cnts += 1

        if people[idx: idx + 2 * M + 1].count(1) == 0 or is_range(idx + 2 * M + 1):
            now_idx = idx + 2 * M + 1
            idx = new_idx(people, now_idx)
        else:
            idx += 2 * M + 1

print(cnts)
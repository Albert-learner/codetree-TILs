import sys

N, K = map(int, input().split())
MAX_N, MAX_K = 100, 10000
n_lst = list(map(int, input().split()))

for _ in range(MAX_N - len(n_lst)):
    n_lst.append(0)

cst = 0
while True:
    cur_min, cur_max = MAX_K, 1
    min_idx, max_idx = 0, 0
    for i in range(N):
        if cur_min > n_lst[i]:
            cur_min = n_lst[i]
            min_idx = i
        if cur_max < n_lst[i]:
            cur_max = n_lst[i]
            max_idx = i

    min_cnts = n_lst.count(cur_min)
    max_cnts = n_lst.count(cur_max)

    if cur_max - cur_min <= K:
        break
    else:
        if min_cnts >= max_cnts:
            n_lst[max_idx] -= 1
            cst += 1
        else:
            n_lst[min_idx] += 1
            cst += 1

print(cst)
from functools import cmp_to_key

N = int(input())
n_lst = list(map(int, input().split()))

answer = []
sort_n_lst = sorted(n_lst)
n_pairs = list(enumerate(sort_n_lst, start = 1))

for n in n_lst:
    if n in list(zip(*n_pairs))[1]:
        n_idx = list(zip(*n_pairs))[1].index(n)
        answer.append(n_pairs[n_idx][0])
        n_pairs.pop(n_idx)

print(*answer)
N = int(input())
n_lst = list(map(int, input().split()))

answer = []
n_pairs = []
sort_n_lst = sorted(n_lst)
for n_idx, n in enumerate(sort_n_lst, 1):
    n_pairs.append([n_idx, n])

for n in n_lst:
    if n in list(zip(*n_pairs))[1]:
        n_idx = list(zip(*n_pairs))[1].index(n)
        answer.append(n_pairs[n_idx][0])

print(*answer)
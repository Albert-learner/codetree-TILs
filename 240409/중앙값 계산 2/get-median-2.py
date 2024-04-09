N = int(input())
n_lst = list(map(int, input().split()))

for n_idx, n in enumerate(n_lst, 1):
    if n_idx % 2 == 1:
        sort_part_n = sorted(n_lst[:n_idx])
        print(sort_part_n[len(sort_part_n) // 2], end = ' ')
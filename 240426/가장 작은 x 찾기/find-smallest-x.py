import math

N = int(input())
ab_lst = [tuple(map(int, input().split())) for _ in range(N)]

x_lst = []
for pair_idx, (a, b) in enumerate(ab_lst, start = 1):
    x_min, x_max = math.ceil(a / 2 ** pair_idx), math.ceil(b / 2 ** pair_idx)
    x_lst.append((x_min, x_max))

x_min_max, x_max_min = max(list(zip(*x_lst))[0]), min(list(zip(*x_lst))[1])
answers = list(range(x_min_max, x_max_min + 1))
print(answers[0])
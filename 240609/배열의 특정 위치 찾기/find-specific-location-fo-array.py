n_lst = list(map(int, input().split()))

evals = [n for idx, n in enumerate(n_lst, 1) if idx % 2 == 0]
threes = [n for idx, n in enumerate(n_lst, 1) if idx % 3 == 0]

print(sum(evals), round(sum(threes) / len(threes), 1))
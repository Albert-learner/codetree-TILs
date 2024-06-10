n_lst = list(map(int, input().split()))

odds = sum([n for idx, n in enumerate(n_lst, 1) if idx % 2 == 1])
evals = sum([n for idx, n in enumerate(n_lst, 1) if idx % 2 == 0])

print(abs(odds - evals))
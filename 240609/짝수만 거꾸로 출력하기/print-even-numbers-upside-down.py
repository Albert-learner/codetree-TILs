N = int(input())
n_lst = [int(input()) for _ in range(N)]

evals = []
for n in n_lst:
    if n % 2 == 0:
        evals.append(n)

for rn in evals[::-1]:
    print(rn, end = ' ')
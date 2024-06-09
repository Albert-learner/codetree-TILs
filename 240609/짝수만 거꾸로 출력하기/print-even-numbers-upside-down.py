N = int(input())
n_lst = list(map(int, input().split()))

evals = []
for n in n_lst:
    if n % 2 == 0:
        evals.append(n)

print(*evals[::-1])
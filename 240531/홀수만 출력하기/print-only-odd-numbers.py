N = int(input())
n_lst = [int(input()) for _ in range(N)]

for n in n_lst:
    if n % 2 == 1 and n % 3 == 0:
        print(n)
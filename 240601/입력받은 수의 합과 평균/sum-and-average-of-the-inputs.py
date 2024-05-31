N = int(input())
n_lst = [int(input()) for _ in range(N)]

print(sum(n_lst), round(sum(n_lst) / N, 1))
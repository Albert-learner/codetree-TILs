N, K = map(int, input().split())
n_lst = list(map(int, input().split()))

n_lst.sort()
print(n_lst[K - 1])
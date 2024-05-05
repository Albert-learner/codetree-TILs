N = int(input())
n_lst = list(map(int, input().split()))
n_lst.sort()

bundles = sorted([(n_lst[i], n_lst[i + N]) for i in range(N)], key = lambda x: abs(x[0] - x[1]))
print(abs(bundles[0][0] - bundles[0][1]))
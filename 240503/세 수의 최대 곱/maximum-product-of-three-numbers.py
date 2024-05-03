N = int(input())
n_lst = list(map(int, input().split()))

n_lst.sort()

max_multiply = n_lst[-1] * n_lst[-2] * n_lst[-3]

max_multiply = max(max_multiply, n_lst[0] * n_lst[1] * n_lst[-1])
print(max_multiply)
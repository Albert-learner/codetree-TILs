N = int(input())
n_lst = list(map(int, input().split()))

print(*[n ** 2 for n in n_lst])
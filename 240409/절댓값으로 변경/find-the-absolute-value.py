N = int(input())
n_lst = list(map(int, input().split()))

print(*[int(abs(n)) for n in n_lst])
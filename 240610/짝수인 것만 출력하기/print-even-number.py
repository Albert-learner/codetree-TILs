N = int(input())
n_lst = list(map(int, input().split()))

print(*[n for n in n_lst if n % 2 == 0])
N = int(input())
n_lst = list(map(int, input().split()))

print(*sorted(n_lst))
print(*list(reversed(sorted(n_lst))))
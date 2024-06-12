N = int(input())
n_lst = list(map(int, input().split()))

twos = []
for idx, n in enumerate(n_lst, 1):
    if n == 2:
        twos.append(idx)

print(twos[2])
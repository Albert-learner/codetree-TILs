n_lst = list(map(int, input().split()))

before_zeros = []
for n in n_lst:
    if n == 0:
        break
    else:
        before_zeros.append(n)

for idx, n in enumerate(before_zeros):
    if n % 2 == 1:
        before_zeros[idx] += 3
    else:
        before_zeros[idx] //= 2

print(*before_zeros)
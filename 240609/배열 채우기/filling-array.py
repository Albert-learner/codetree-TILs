n_lst = list(map(int, input().split()))

arr = []
for n in n_lst:
    if n == 0:
        break
    else:
        arr.append(n)

print(*arr[::-1])
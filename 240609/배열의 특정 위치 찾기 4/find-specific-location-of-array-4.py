n_lst = list(map(int, input().split()))

twos = []
for n in n_lst:
    if n == 0:
        break
    elif n % 2 == 0:
        twos.append(n)

print(len(twos), sum(twos))
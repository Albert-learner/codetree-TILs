n_lst = [int(input()) for _ in range(10)]

odds = 0
for n in n_lst:
    if n % 2 == 1:
        odds += 1

print(odds)
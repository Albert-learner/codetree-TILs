n_lst = [int(input()) for _ in range(5)]

print(len([n for n in n_lst if n % 2 == 0]))
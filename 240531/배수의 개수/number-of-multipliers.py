n_lst = [int(input()) for _ in range(10)]

print(len([n for n in n_lst if n % 3 == 0]), len([n for n in n_lst if n % 5 == 0]))
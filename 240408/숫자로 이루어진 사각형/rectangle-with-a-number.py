def print_rectangle(n):
    quota, rest = divmod(n ** 2, 9)
    nums_lst = quota * list(range(1, 10)) + list(range(1, rest + 1))

    for num_idx, num in enumerate(nums_lst, 1):
        if num_idx % n == 0:
            print(num)
        else:
            print(num, end = ' ')
    

N = int(input())
print_rectangle(N)
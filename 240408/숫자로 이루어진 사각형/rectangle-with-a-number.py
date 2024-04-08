def print_rectangle(n):
    nums_lst = [num if num <= 9 else int(str(num + 1)[-1]) for num in range(1, n ** 2 + 1)]
    
    for num_idx, num in enumerate(nums_lst, 1):
        if num_idx % n == 0:
            print(num)
        else:
            print(num, sep=' ', end=' ')


N = int(input())
print_rectangle(N)
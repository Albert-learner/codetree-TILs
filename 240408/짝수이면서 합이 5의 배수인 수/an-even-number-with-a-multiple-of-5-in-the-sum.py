N = int(input())

nums_lst = [int(n_str) for n_str in str(N)]

if N % 2 == 0 and sum(nums_lst) % 5 == 0:
    print("Yes")
else:
    print("No")
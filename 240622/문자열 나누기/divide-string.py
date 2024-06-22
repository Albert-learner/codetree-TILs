N = int(input())
nums_str = "".join(input().split())

for idx, n_str in enumerate(nums_str, 1):
    if idx % 5 == 0:
        print(n_str)
    else:
        print(n_str, end = '')
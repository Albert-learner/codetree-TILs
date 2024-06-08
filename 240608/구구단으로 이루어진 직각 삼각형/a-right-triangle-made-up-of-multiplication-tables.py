N = int(input())

nums = N
for i in range(1, N + 1):
    for j in range(1, nums + 1):
        if j == nums:
            print(f"{i} * {j} = {i * j}")
        else:
            print(f"{i} * {j} = {i * j} /", end = ' ')
    nums -= 1
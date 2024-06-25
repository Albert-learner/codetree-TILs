N = int(input())
nums = [int(input()) for _ in range(N)]

total = sum(nums)
print(str(total)[1:] + str(total)[0])
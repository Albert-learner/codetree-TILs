nums = [int(input()) for _ in range(5)]

if all(n % 3 == 0 for n in nums):
    print(1)
else:
    print(0)
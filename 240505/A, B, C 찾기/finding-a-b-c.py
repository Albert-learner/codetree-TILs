nums = list(map(int, input().split()))
nums.sort()

a, b, c = 0, 0, 0
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        for k in range(j + 1, len(nums)):
            if nums[i] + nums[j] + nums[k] == nums[-1]:
                a, b, c = nums[i], nums[j], nums[k]
                break

print(a, b, c)
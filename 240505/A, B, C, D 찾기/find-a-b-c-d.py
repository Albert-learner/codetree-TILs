nums = list(map(int, input().split()))
nums.sort()

a, b, c, d = 0, 0, 0, 0
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        for k in range(j + 1, len(nums)):
            for l in range(k + 1, len(nums)):
                if nums[i] <= nums[j] <= nums[k] <= nums[l] and nums[k] <= nums[i] + nums[j] and nums[i] + nums[j] + nums[k] + nums[l] == nums[-1]:
                    a, b, c, d = nums[i], nums[j], nums[k], nums[l]
                    break

print(a, b, c, d)
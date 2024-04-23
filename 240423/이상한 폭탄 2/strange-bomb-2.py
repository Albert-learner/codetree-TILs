N, K = map(int, input().split())
nums = [int(input()) for _ in range(N)]

answer = -1
explode_nums = []
nums_cnt = dict.fromkeys(sorted(set(nums)), 0)

for num_idx, num in enumerate(nums):
    if num_idx < K and num in nums[num_idx + 1:num_idx + K + 1]:
        explode_nums.append(num)
    elif num_idx + K <= len(nums) - 1 and num in nums[num_idx + 1:]:
        explode_nums.append(num)
    elif K <= num_idx < len(nums) + K - 1 and num in nums[num_idx - K // 2:num_idx + K // 2]:
        explode_nums.append(num)

print(max(set(explode_nums)))
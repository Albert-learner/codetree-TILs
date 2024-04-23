N, K = map(int, input().split())
nums = [int(input()) for _ in range(N)]

answer = -1
for i in range(N):
    bomb_num = -1
    for j in range(i + 1, i + K + 1):
        if j - i > K or j > len(nums) - 1:
            continue

        if nums[i] == nums[j]:
            bomb_num = nums[i]

    answer = max(answer, bomb_num)

print(answer)
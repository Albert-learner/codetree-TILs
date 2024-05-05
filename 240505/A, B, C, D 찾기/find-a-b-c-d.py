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

# # 모범답안
# n = 15

# # 변수 선언 및 입력
# arr = list(map(int, input().split()))

# # 오름차순으로 정렬을 진행합니다.
# arr.sort()

# # 오름차순으로 정렬했을 때,
# # 가장 작은 숫자는 A,
# # 두 번째로 작은 숫자 B,
# # 그리고 세 번째로 작은 숫자는 C가 됩니다.
# a, b, c = arr[0], arr[1], arr[2]
# # 또한, 가장 큰 숫자는 항상 A + B + C + D가 되므로
# # D 는 끝 숫자 - A - B - C가 됩니다
# d = arr[-1] - a - b - c

# print(a, b, c, d)
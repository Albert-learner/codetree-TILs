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

# # 모범답안
# n = 7

# # 변수 선언 및 입력
# arr = list(map(int, input().split()))

# # 오름차순으로 정렬을 진행합니다.
# arr.sort()

# # 오름차순으로 정렬했을 때,
# # 가장 작은 숫자는 A,
# # 두 번째로 작은 숫자는 항상 B가 됩니다.
# a , b = arr[0], arr[1]
# # 또한, 가장 큰 숫자는 항상 A + B + C가 되므로
# # C 는 끝 숫자 - A - B가 됩니다
# c = arr[-1] - a - b

# print(a, b, c)
nums = [list(map(int, input().split())) for _ in range(2)]

for row in nums:
    print("{:.1f}".format(sum(row) / len(row)), end = ' ')
print()

for col in range(len(nums[0])):
    row_sum = sum([nums[row][col] for row in range(len(nums))])
    print("{:.1f}".format(row_sum / len(nums)), end = ' ')
print()

one_d_lst = sum(nums, [])
print("{:.1f}".format(sum(one_d_lst) / len(one_d_lst)))
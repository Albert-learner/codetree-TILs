n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
nums_set_lst = sorted(list(set(arr)))
nums_pos = {}
for num in nums_set_lst:
    if num in arr:
        nums_pos[num] = arr.index(num)

for num, num_pos in list(nums_pos.items()):
    print(num, num_pos + 1)



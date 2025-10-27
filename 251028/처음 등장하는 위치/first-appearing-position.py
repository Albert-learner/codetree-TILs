n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
nums_set_lst = sorted(list(set(arr)))

for num in nums_set_lst:
    for num_idx in range(len(arr)):
        if arr[num_idx] == num:
            print(num, num_idx + 1)
            break


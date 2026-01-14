s = int(input())

# Please write your code here.
s_sum, num = 0, 0

while s_sum < s:
    num += 1
    s_sum += num

if s_sum > s:
    print(num - 1)
else:
    print(num)
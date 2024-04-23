X, Y = map(int, input().split())
nums_lst = list(range(X, Y + 1))

convert_nums = sorted([[int(digit) for digit in str(num)] for num in nums_lst], key = lambda x: sum(x), reverse = True)
print(sum(convert_nums[0]))
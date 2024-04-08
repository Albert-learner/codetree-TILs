A, B = map(int, input().split())

nums_lst = [num for num in range(A, B + 1) if num % 3 == 0 or '3' in str(num) or '6' in str(num) or '9' in str(num)]

print(len(nums_lst))
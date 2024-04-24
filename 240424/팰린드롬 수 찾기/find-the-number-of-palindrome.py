X, Y = map(int, input().split())
nums_lst = list(range(X, Y + 1))

def is_palindrome(num):
    if num == num[::-1]:
        return True
    else:
        return False

cnts = 0
for num in nums_lst:
    num_lst = list(map(int, str(num)))
    if is_palindrome(num_lst):
        cnts += 1

print(cnts)
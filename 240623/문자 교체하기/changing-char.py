first, second = input().split()
first_lst, second_lst = list(first), list(second)

second_lst[:2] = first_lst[:2]
print("".join(second_lst))
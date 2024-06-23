input_str_lst = list(input())

input_str_lst[1], input_str_lst[-2] = 'a', 'a'
print("".join(input_str_lst))
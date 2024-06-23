input_str_lst = list(input())

input_str_lst[0], input_str_lst[1] = input_str_lst[1], input_str_lst[0]
for idx, inp_chr in enumerate(input_str_lst[2:], 2):
    if inp_chr == input_str_lst[0]:
        input_str_lst[idx] = input_str_lst[1]
    elif inp_chr == input_str_lst[1]:
        input_str_lst[idx] = input_str_lst[0]

print("".join(input_str_lst))
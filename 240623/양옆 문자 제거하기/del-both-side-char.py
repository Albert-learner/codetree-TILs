input_str_lst = list(input())

rem_lst = []
for idx, inp_chr in enumerate(input_str_lst, 1):
    if idx != 2 and idx != len(input_str_lst) - 1:
        rem_lst.append(inp_chr)
    
print("".join(rem_lst))
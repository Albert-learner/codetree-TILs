input_str_lst = list(input())

while len(input_str_lst) > 1:
    idx = int(input())

    if idx >= len(input_str_lst):
        input_str_lst.pop()
    else:
        input_str_lst.pop(idx)

    print("".join(input_str_lst))
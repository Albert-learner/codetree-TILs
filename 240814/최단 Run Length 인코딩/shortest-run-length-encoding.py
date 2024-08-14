from collections import deque

a_str = input()

def run_length_encoding(input_str):
    result = ""
    indices = [-1]
    for chr_idx in range(len(input_str) - 1):
        if input_str[chr_idx] != input_str[chr_idx + 1]:
            indices.append(chr_idx)
    indices.append(len(input_str) - 1)

    cnts_lst = []
    for i in range(len(indices) - 1):
        diff = indices[i + 1] - indices[i]
        cnts_lst.append(diff)

    for chr_idx, cnts in zip(indices[1:], cnts_lst):
        result += (input_str[chr_idx] + str(cnts))

    return result

min_length = len(a_str)
for cnts in range(1, len(a_str)):
    a_str_que = deque(a_str)
    a_str_que.rotate(cnts)
    a_str_rotate = "".join(a_str_que)

    encoding = len(run_length_encoding(a_str_rotate))
    min_length = min(min_length, encoding)

print(min_length)
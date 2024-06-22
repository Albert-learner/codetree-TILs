input_str = input()

def run_length_encoding(input_str):
    ret_str = ""
    
    indices = [-1]
    for i in range(len(input_str) - 1):
        if input_str[i] != input_str[i + 1]:
            indices.append(i)
    indices.append(len(input_str) - 1)
    
    cnts_lst = []
    for i in range(len(indices) - 1):
        diff = indices[i + 1] - indices[i]
        cnts_lst.append(diff)

    for chr_idx, cnts in zip(indices[1:], cnts_lst):
        ret_str += (input_str[chr_idx] + str(cnts))

    return ret_str

answer = run_length_encoding(input_str)
print(len(answer))
print(answer)
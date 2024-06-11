input_chr = input()

chr_lst = ['L', 'E', 'B', 'R', 'O', 'S']
if input_chr in chr_lst:
    idx = 0
    for elem_idx, elem in enumerate(chr_lst):
        if elem == input_chr:
            idx = elem_idx
            break
    print(idx)
else:
    print("None")
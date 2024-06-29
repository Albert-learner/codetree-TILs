ch_bin_num = input()
ch_bin_num_lst = list(ch_bin_num)

max_cst = 0
if '0' not in ch_bin_num_lst:
    ch_bin_num_lst[-1] = '0'
else:
    for b_n_idx, bin_n in enumerate(ch_bin_num_lst):
        if bin_n == '0':
            ch_bin_num_lst[b_n_idx] = '1'
            break

for base_num, bin_n in enumerate(ch_bin_num_lst[::-1]):
        max_cst += int(bin_n) * (2 ** base_num)
print(max_cst)
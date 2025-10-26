inp_str = input()

# Please write your code here.
from collections import Counter

chr_cnts = 0
str_cntr = Counter(inp_str)

for inp_chr, cnts in str_cntr.items():
    if cnts == 1:
        chr_cnts += 1
        print(inp_chr)
        break

if chr_cnts == 0:
    print(None)
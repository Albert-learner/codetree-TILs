a_bin = input()

zero_cnts = a_bin.count('0') if a_bin.count('0') > 1 else 1
zero_cnts -= 1

bin_lst = [1 for _ in range(len(a_bin))]
for i in range(zero_cnts):
    bin_lst[-i - 1] = 0

num = 0
for idx in range(len(bin_lst)):
    num = num * 2 + bin_lst[idx]

print(num)
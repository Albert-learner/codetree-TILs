bin_number = input()

bin_lst = list(map(int, bin_number))
num = 0

for i in range(len(bin_lst)):
    num = num * 2 + bin_lst[i]

print(num)
n_lst = list(map(int, input().split()))

nums = []
for n in n_lst:
    if n == 0:
        break
    else:
        nums.append(n)

ten_nums = [int(str(num)[0]) for num in nums if len(str(num)) >= 2]
tens_cntr = {n: 0 for n in range(1, 10)}

for ten_num in ten_nums:
    if ten_num in tens_cntr:
        tens_cntr[ten_num] += 1

for ten_num, cnts in tens_cntr.items():
    print(f"{ten_num} - {cnts}")
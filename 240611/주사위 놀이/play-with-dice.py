nums = list(map(int, input().split()))

nums_cntr = {n: 0 for n in range(1, 7)}
for n in nums:
    if n in nums_cntr:
        nums_cntr[n] += 1

for n, cnts in nums_cntr.items():
    print(f"{n} - {cnts}")
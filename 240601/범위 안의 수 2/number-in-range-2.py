n_lst = [int(input()) for _ in range(10)]

cnts = [n for n in n_lst if 0 <= n <= 200]
totals = sum(cnts)
avgs = round(totals / len(cnts), 1)

print(totals, avgs)
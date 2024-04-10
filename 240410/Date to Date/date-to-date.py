m1, d1, m2, d2 = map(int, input().split())

month_days = [(1, 31), (2, 28), (3, 31), (4, 30), (5, 31), (6, 30), (7, 31), (8, 31), (9, 30), (10, 31), (11, 30), (12, 31)]

start_date = sum([days for month, days in month_days if month <= m1 - 1]) + d1
end_date = sum([days for month, days in month_days if month <= m2 - 1]) + d2

print(end_date - start_date + 1)
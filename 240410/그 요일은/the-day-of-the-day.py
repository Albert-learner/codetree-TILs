m1, d1, m2, d2 = map(int, input().split())
find_day = input()

month_days = [(1, 31), (2, 28), (3, 31), (4, 30), (5, 31), (6, 30), (7, 31), (8, 31), (9, 30), (10, 31), (11, 30), (12, 31)]

start_date = sum([days for month, days in month_days if month <= m1 - 1]) + d1
end_date = sum([days for month, days in month_days if month <= m2 - 1]) + d2

days = {"Mon": 0, "Tue": 1, "Wed": 2, "Thu": 3, "Fri": 4, "Sat": 5, "Sun": 6}
find_day_num = days[find_day]

quota, rest = divmod(end_date - start_date + 1, 7)
if rest < find_day_num:
    print(quota)
else:
    print(quota + 1)
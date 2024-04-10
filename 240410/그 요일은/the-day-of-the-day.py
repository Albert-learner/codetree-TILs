m1, d1, m2, d2 = map(int, input().split())
find_day = input()

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def get_num(f_day):
    for day_idx, day in enumerate(days):
        if day == f_day:
            return day_idx

day_num = get_num(find_day)
d1 += day_num

def total_days(m, d):
    t_days = 0
    for i in range(m):
        t_days += months[i]

    t_days += d

    return t_days

diff_days = total_days(m2, d2) - total_days(m1, d1)
print(diff_days // 7 + 1)
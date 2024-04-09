Y, M, D = map(int, input().split())

def is_leap_year(y):
    if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
        return True
    
    return False

def is_wrong_day(y, m, d):
    if m in [4, 6, 9, 11] and d > 30:
        return True
    elif m == 2 and is_leap_year(y) and d > 29:
        return True
    elif m == 2 and is_leap_year(y) == False and d > 28:
        return True
    else:
        return False

if is_wrong_day(Y, M, D):
    print(-1)
else:
    if M in [12, 1, 2]:
        print("Winter")
    elif M in [3, 4, 5]:
        print("Spring")
    elif M in [6, 7, 8]:
        print("Summer")
    elif M in [9, 10, 11]:
        print("Fall")
    else:
        print(-1)
Y, M, D = map(int, input().split())

def is_leap_year(y):
    if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
        return True
    
    return False

def is_right_day(y, m, d):
    if not is_leap_year(y):
        if m in [12, 1, 2]:
            if m in [12, 1]:
                if d in range(1, 32):
                    return "Winter"
                else:
                    return -1
            else:
                if d in range(1, 32):
                    return "Winter"
                else:
                    return -1
        elif m in [3, 4, 5]:
            if m in [3, 5]:
                if d in range(1, 32):
                    return "Spring"
                else:
                    return -1
            else:
                if d in range(1, 31):
                    return "Spring"
                else:
                    return -1
        elif m in [6, 7, 8]:
            if m in [7, 8]:
                if d in range(1, 32):
                    return "Summer"
                else:
                    return -1
            else:
                if d in range(1, 31):
                    return "Summer"
                else:
                    return -1
        elif m in [9, 10, 11]:
            if m == 10:
                if d in range(1, 32):
                    return "Fall"
                return -1
            else:
                if d in range(1, 31):
                    return "Fall"
                else:
                    return -1
        else:
            return -1
    else:
        if m != 2:
            if m in [12, 1]:
                if d in range(1, 32):
                    return "Winter"
                else:
                    return -1
            elif m in [3, 4, 5]:
                if m in [3, 5]:
                    if d in range(1, 32):
                        return "Spring"
                    else:
                        return -1
                else:
                    if d in range(1, 31):
                        return "Spring"
                    else:
                        return -1
            elif m in [6, 7, 8]:
                if m in [7, 8]:
                    if d in range(1, 32):
                        return "Summer"
                    else:
                        return -1
                else:
                    if d in range(1, 31):
                        return "Summer"
                    else:
                        return -1
            elif m in [9, 10, 11]:
                if m == 10:
                    if d in range(1, 32):
                        return "Fall"
                    else:
                        return -1
                else:
                    if d in range(1, 31):
                        return "Fall"
                    else:
                        return -1
            else:
                return -1
        else:
            if d in range(1, 30):
                return "Winter"
            else:
                return False
    
print(is_right_day(Y, M, D))
y = int(input())

def leap_disriminate(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True

    return False

print("true" if leap_disriminate(y) else "false")
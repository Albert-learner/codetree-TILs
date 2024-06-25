a_str = input()
b_str = input()

min_n = 0
cnts = 0
while cnts < len(a_str):
    if a_str != b_str:
        a_str = a_str[-1] + a_str[:-1]
    else:
        min_n = cnts
        break

    cnts += 1

if min_n == 0:
    print(-1)
else:
    print(min_n)
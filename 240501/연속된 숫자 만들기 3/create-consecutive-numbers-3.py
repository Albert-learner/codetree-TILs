first, second, third = map(int, input().split())
first, second, third = sorted([first, second, third])

f_dst = abs(first - second)
s_dst = abs(second - third)

cnts = 0
if f_dst == 1 and s_dst == 1:
    cnts = 0
elif f_dst <= 2 and s_dst <= 2:
    cnts = 1
else:
    cnts = max(f_dst, s_dst) - 1

print(cnts)
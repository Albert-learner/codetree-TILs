first, second, third = map(int, input().split())
first, second, third = sorted([first, second, third])

min_move = 0
while True:
    f_s_diff = abs(first - second)
    s_t_diff = abs(second - third)
    
    if f_s_diff == 1 and s_t_diff == 1:
        break

    if f_s_diff == 2 or s_t_diff == 2:
        min_move += 1
        break
    elif f_s_diff > 2 and s_t_diff > 2:
        if f_s_diff < s_t_diff:
            second, third = first + 2, second
        else:
            first, second = second, second + 2
    elif abs(second - third) > 2:
        first, second = second, second + 2
    elif abs(first - second) > 2:
        second, third = first + 2, second

    min_move += 1

print(min_move)
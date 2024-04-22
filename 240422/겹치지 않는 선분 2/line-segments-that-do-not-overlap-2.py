N = int(input())
lines = [list(map(int, input().split())) for _ in range(N)]

def check_cross(num):
    some = 0

    p0 = lines[num][0]
    p1 = lines[num][1]
    p_diff = p1 - p0

    for p in range(N):
        if p == num:
            continue

        cp0, cp1 = lines[p][0], lines[p][1]
        cp_diff = cp1 - cp0

        up = p0 * cp_diff - cp0 * p_diff
        down = cp_diff - p_diff

        if down != 0:
            result = up / down

            if min(p0, p1) <= result <= max(p0, p1) and min(cp0, cp1) <= result <= max(cp0, cp1):
                some += 1
    
    if some == 0:
        return True
    else:
        return False

cnts = 0
for i in range(N):
    if check_cross(i):
        cnts += 1

print(cnts)
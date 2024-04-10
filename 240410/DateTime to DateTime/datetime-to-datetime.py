A, B, C = map(int, input().split())

if A >= 11 or B >= 11 or C >= 11:
    day_diff, hour_diff, minute_diff = A - 11, B - 11, C - 11
    print(day_diff * 24 * 60 + hour_diff * 60 + minute_diff)
else:
    print(-1)
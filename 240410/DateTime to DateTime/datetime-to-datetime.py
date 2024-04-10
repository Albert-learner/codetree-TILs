A, B, C = map(int, input().split())

if not(A < 11 and B < 11 and C < 11):
    day_diff = A - 11
    hour_diff = B - 11
    minute_diff = C - 11
    print(day_diff * 24 * 60 + hour_diff * 60 + minute_diff)
else:
    print(-1)
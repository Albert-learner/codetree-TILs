A, B, C = map(int, input().split())

start_time = (11 - 1) * 24 * 60 + 11 * 60 + 11
end_time = (A - 1) * 24 * 60 + B * 60 + C

if end_time - start_time < 0:
    print(-1)
else:
    print(end_time - start_time)
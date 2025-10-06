N, M = map(int, input().split())
numbers = list(map(int, input().split()))

NEG = -10 ** 18

dp0 = [NEG] * (M + 1)
dp1 = [NEG] * (M + 1)
dp0[0] = 0  

for x in numbers:
    ndp0 = [NEG] * (M + 1)
    ndp1 = [NEG] * (M + 1)
    for k in range(M + 1):
        if dp0[k] != NEG or dp1[k] != NEG:
            ndp0[k] = max(ndp0[k], dp0[k], dp1[k])


        if dp1[k] != NEG:
            ndp1[k] = max(ndp1[k], dp1[k] + x)
        if k >= 1 and dp0[k - 1] != NEG:
            ndp1[k] = max(ndp1[k], dp0[k - 1] + x)

    dp0, dp1 = ndp0, ndp1

print(max(dp0[M], dp1[M]))

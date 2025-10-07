n = input()

# Please write your code here.
MOD = 10 ** 9 + 7
dp = [[[[0] * 2 for _ in range(2)] for _ in range(3)] for _ in range(2)]
dp[1][0][0][0] = 1

in369 = [False]*10
for d in (3, 6, 9):
    in369[d] = True

for ch in n:
    limit = ord(ch) - 48
    ndp = [[[[0] * 2 for _ in range(2)] for _ in range(3)] for _ in range(2)]
    for tight in (0, 1):
        hi = limit if tight == 1 else 9
        for mod3 in range(3):
            for seen in (0, 1):
                for started in (0, 1):
                    ways = dp[tight][mod3][seen][started]
                    if ways == 0:
                        continue
                    for d in range(hi + 1):
                        ntight = 1 if (tight == 1 and d == hi) else 0
                        nstarted = 1 if (started == 1 or d != 0) else 0
                        nmod3 = (mod3 + d) % 3 if nstarted else 0
                        nseen = seen
                        if nstarted and in369[d]:
                            nseen = 1
                        ndp[ntight][nmod3][nseen][nstarted] = (ndp[ntight][nmod3][nseen][nstarted] + ways) % MOD
    dp = ndp

ans = 0
for tight in (0, 1):
    for mod3 in range(3):
        for seen in (0, 1):
            if seen == 1 or mod3 == 0:
                ans = (ans + dp[tight][mod3][seen][1]) % MOD

print(ans)
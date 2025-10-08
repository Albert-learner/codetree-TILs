n = int(input())
s = []
b = []
for _ in range(n):
    si, bi = map(int, input().split())
    s.append(si)
    b.append(bi)

# Please write your code here.
S, B = 11, 9
NEG = -10 ** 18

dp = [[NEG] * (B + 1) for _ in range(S + 1)]
dp[0][0] = 0

for i in range(n):
    si, bi = s[i], b[i]
    ndp = [row[:] for row in dp]

    for x in range(S + 1):
        for y in range(B + 1):
            if dp[x][y] == NEG:
                continue

            if x + 1 <= S:
                if ndp[x + 1][y] < dp[x][y] + si:
                    ndp[x + 1][y] = dp[x][y] + si

            if y + 1 <= B:
                if ndp[x][y + 1] < dp[x][y] + bi:
                    ndp[x][y + 1] = dp[x][y] + bi

    dp = ndp

print(dp[S][B])
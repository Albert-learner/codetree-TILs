n = int(input())
points = [0] + list(map(int, input().split()))

# Please write your code here.
MOD = 10007

if n == 1:
    print(1)
elif points[1] >= points[n]:
    print(0)
else:
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    dp[1][1] = 1

    for cur in range(2, n):
        new_dp = [row[:] for row in dp]

        for go_last in range(1, n + 1):
            for back_last in range(1, n + 1):
                val = dp[go_last][back_last]
                if val == 0:
                    continue

                if points[go_last] < points[cur] < points[n]:
                    new_dp[cur][back_last] = (new_dp[cur][back_last] + val) % MOD

                if points[back_last] < points[cur] < points[n]:
                    new_dp[go_last][cur] = (new_dp[go_last][cur] + val) % MOD

        dp = new_dp

    answer = 0

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if points[i] < points[n] and points[j] < points[n]:
                answer = (answer + dp[i][j]) % MOD

    print(answer)
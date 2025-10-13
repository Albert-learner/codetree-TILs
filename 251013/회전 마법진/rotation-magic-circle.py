N = int(input())
a = input()
b = input()

# Please write your code here.
A = [int(ch) for ch in a]
B = [int(ch) for ch in b]

INF = 10 ** 18
dp = [[INF] * 10 for _ in range(N + 1)]
for c in range(10):
    dp[N][c] = 0

for i in range(N - 1, -1, -1):
    for carry in range(10):
        cur = (A[i] + carry) % 10
        target = B[i]
        for l in range(10):
            after_left = (cur + l) % 10
            y = (after_left - target) % 10
            next_carry = (carry + l) % 10
            dp[i][carry] = min(dp[i][carry], l + y + dp[i + 1][next_carry])

print(dp[0][0])
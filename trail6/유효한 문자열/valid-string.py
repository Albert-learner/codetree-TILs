str = input()

# Please write your code here.
MOD = 10007
s = str
n = len(s)

def match_count(a, b):
    pairs = [('(', ')'), ('[', ']'), ('{', '}')]
    cnt = 0

    for open_ch, close_ch in pairs:
        if (a == open_ch or a == '?') and ( b == close_ch or b == '?'):
            cnt += 1

    return cnt

if n % 2 == 1:
    print(0)
else:
    dp = [[0] * n for _ in range(n)]

    for length in range(2, n + 1, 2):
        for left in range(0, n - length + 1):
            right = left + length - 1

            for mid in range(left + 1, right + 1, 2):
                cnt = match_count(s[left], s[mid])

                if cnt == 0:
                    continue

                inside = 1 if mid == left + 1 else dp[left + 1][mid - 1]
                outside = 1 if mid == right else dp[mid + 1][right]

                dp[left][right] += cnt * inside * outside
                dp[left][right] %= MOD

    print(dp[0][n - 1])
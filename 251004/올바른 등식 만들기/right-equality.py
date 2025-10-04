N, M = map(int, input().split())
nums = list(map(int, input().split()))

OFFSET = 20
RANGE = 2 * OFFSET + 1  # -20..20 -> 41칸

dp = [0] * RANGE

first = nums[0]
if -20 <= first <= 20:
    dp[first + OFFSET] += 1
if first != 0 and -20 <= -first <= 20:
    dp[-first + OFFSET] += 1

for x in nums[1:]:
    ndp = [0] * RANGE
    for s in range(RANGE):
        ways = dp[s]
        if ways == 0:
            continue
        cur = s - OFFSET

        plus = cur + x
        if -20 <= plus <= 20:
            ndp[plus + OFFSET] += ways

        minus = cur - x
        if -20 <= minus <= 20:
            ndp[minus + OFFSET] += ways
    dp = ndp

print(dp[M + OFFSET] if -20 <= M <= 20 else 0)

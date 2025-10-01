n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
S = sum(arr)
NEG = -10**15

dp = [NEG] * (S + 1)
dp[0] = 0 

for x in arr:
    ndp = dp[:]
    for delta in range(S + 1):
        b = dp[delta]
        if b == NEG:
            continue
        a = b + delta

        if delta + x <= S:
            ndp[delta + x] = max(ndp[delta + x], b)

        if x <= delta:
            ndp[delta - x] = max(ndp[delta - x], b + x)
        else:
            new_delta = x - delta
            if new_delta <= S:
                ndp[new_delta] = max(ndp[new_delta], a)

    dp = ndp

ans = dp[0]
if ans < 0:
    ans = 0 
print(ans)

n, k = map(int, input().split())
inp_str = input()

# Please write your code here.
NEG = -10 ** 9
dp = [[[NEG] * 2 for _ in range(k + 1)] for _ in range(n)]

dp[0][0][0] = 1 if inp_str[0] == 'L' else 0 
dp[0][0][1] = NEG                              
if k >= 1:
    dp[0][1][1] = 1 if inp_str[0] == 'R' else 0     
    
for i in range(1, n):
    for j in range(k+1):
        stay_left = dp[i - 1][j][0]
        move_to_left = dp[i - 1][j - 1][1] if j > 0 else NEG
        dp[i][j][0] = max(stay_left, move_to_left) + (1 if inp_str[i] == 'L' else 0)

        stay_right = dp[i - 1][j][1]
        move_to_right = dp[i - 1][j - 1][0] if j > 0 else NEG
        dp[i][j][1] = max(stay_right, move_to_right) + (1 if inp_str[i] == 'R' else 0)

ans = max(dp[n-1][j][p] for j in range(k+1) for p in range(2))
print(ans)
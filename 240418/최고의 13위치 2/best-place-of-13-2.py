N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

answer = 0
for i in range(N):
    for j in range(N - 2):
        for k in range(N):
            for l in range(N - 2):
                if i == k and abs(l - j) <= 2:
                    continue

                cnt1 = grid[i][j] + grid[i][j + 1] + grid[i][j + 2]
                cnt2 = grid[k][l] + grid[k][l + 1] + grid[k][l + 2]
                answer = max(answer, cnt1 + cnt2)

print(answer)
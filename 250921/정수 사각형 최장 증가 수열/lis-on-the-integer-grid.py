n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
cells = []
for i in range(n):
    for j in range(n):
        cells.append((grid[i][j], i, j))
cells.sort()

dp = [[1] * n for _ in range(n)]
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for val, x, y in cells:
    best = 1
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] < val:
            if dp[nx][ny] + 1 > best:
                best = dp[nx][ny] + 1

    dp[x][y] = best

print(max(max(row) for row in dp))
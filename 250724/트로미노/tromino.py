N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

# Please write your code here.
def return_max1(x, y, board):
    max_sum = board[x][y] + board[x + 1][y] + board[x][y + 1] + board[x + 1][y + 1]
    answer = 0

    for i in range(x, x + 2):
        for j in range(y, y + 2):
            cur_sum = max_sum - board[i][j]
            answer = max(answer, cur_sum)

    return answer

max_sum = 0
for i in range(N - 1):
    for j in range(M - 1):
        max_sum = max(max_sum, return_max1(i, j, grid))

for i in range(N):
    for j in range(M - 2):
        max_sum = max(max_sum, grid[i][j] + grid[i][j + 1] + grid[i][j + 2])

for j in range(M):
    for i in range(N - 2):
        max_sum = max(max_sum, grid[i][j] + grid[i + 1][j] + grid[i + 2][j])
print(max_sum)
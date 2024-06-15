N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

def return_max1(x, y, board):
    max_sum = board[x][y] + board[x + 1][y] + board[x][y + 1] + board[x + 1][y + 1]
    answer = 0

    for i in range(x, x + 2):
        for j in range(y, y + 2):
            now_sum = max_sum - board[i][j]
            answer = max(answer, now_sum)
    
    return answer

max_value = 0
for i in range(N - 1):
    for j in range(M - 1):
        max_value = max(max_value, return_max1(i, j, board))

for i in range(N):
    for j in range(M - 2):
        max_value = max(max_value, board[i][j] + board[i][j + 1] + board[i][j + 2])

for j in range(M):
    for i in range(N - 2):
        max_value = max(max_value, board[i][j] + board[i + 1][j] + board[i + 2][j])

print(max_value)
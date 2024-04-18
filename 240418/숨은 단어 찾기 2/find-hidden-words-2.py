N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

chk_dirs = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]

answer = 0
for i in range(len(board)):
    for j in range(len(board[0])):
        for di, dj in chk_dirs:
            if 0 <= i + 2 * di < N and 0 <= j + 2 * dj < M:
                if board[i][j] == 'L' and board[i + di][j + dj] == 'E' and board[i + 2 * di][j + 2 * dj] == 'E':
                    answer += 1
            else:
                continue

print(answer)
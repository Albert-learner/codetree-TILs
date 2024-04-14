N = int(input())
board = [list(input()) for _ in range(N)]
K = int(input())

dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]

slash_dir = {
    0: 1,
    1: 0,
    2: 3,
    3: 2
}

rev_slash_dir = {
    0: 3,
    1: 2,
    2: 1,
    3: 0
}

lazer_start_dir = 0
r, c = 0, 0

if K <= N:
    lazer_start_dir = 0
    r, c = 0, K - 1
elif N < K and K <= 2 * N:
    lazer_start_dir = 1
    r, c = K - N - 1, N - 1
elif 2 * N < K and K <= 3 * N:
    lazer_start_dir = 2
    r, c = N - 1, 3 * N - K
elif K > 3 * N:
    lazer_start_dir = 3
    r, c = 4 * N - K, 0

cnts = 0
while 0 <= r < N and 0 <= c < N:
    if board[r][c] == '/':
        lazer_start_dir = slash_dir[lazer_start_dir]
    elif board[r][c] == '\\':
        lazer_start_dir = rev_slash_dir[lazer_start_dir]

    r, c = r + dx[lazer_start_dir], c + dy[lazer_start_dir]
    cnts += 1

print(cnts)
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

row_diff, col_diff = len(board) - 3, len(board[0]) - 3
max_coins = 0

if row_diff == 0 and col_diff == 0:
    for r in range(len(board)):
        for c in range(len(board[0])):
            max_coins += board[r][c]
else:
    coins_lst = []
    for r in range(row_diff):
        for c in range(col_diff):
            coins = 0
            for k in range(3):
                for l in range(3):
                    coins += board[r + k][c + l]
            max_coins = max(max_coins, coins)

print(max_coins)
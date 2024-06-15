N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

max_coins = 0
for i in range(N - 2):
    for j in range(N - 2):
        coins = 0
        for r in board[i:i + 3]:
            coins += sum(r[j:j + 3])
        max_coins = max(max_coins, coins)

print(max_coins)
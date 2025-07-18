N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

# Please write your code here.
max_coins = 0
for i in range(N - 2):
    for j in range(N - 2):
        coins = 0
        for row in board[i:i + 3]:
            coins += sum(row[j: j + 3])

        max_coins = max(max_coins, coins)

print(max_coins)
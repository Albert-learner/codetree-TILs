n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
max_coins = 0

for i in range(n - 2):
    for j in range(n - 2):
        coins = 0
        for row in grid[i:i + 3]:
            coins += sum(row[j:j + 3])

        max_coins = max(max_coins, coins)

print(max_coins)
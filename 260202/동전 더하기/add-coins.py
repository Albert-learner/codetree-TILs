n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

# Please write your code here.
coins.sort(reverse = True)

cnts = 0
for coin in coins:
    if k == 0:
        break

    cnts += k // coin
    k %= coin

print(cnts)
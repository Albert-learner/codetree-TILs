N, B = map(int, input().split())
prices = [int(input()) for _ in range(N)]
prices.sort()

max_cnts = 0
for i in range(N):
    cnts = 0
    satisfy = B
    for j in range(N):
        price = prices[j] // 2 if j == i else prices[j]

        if satisfy >= price:
            satisfy -= price
            cnts += 1

    max_cnts = max(max_cnts, cnts)

print(max_cnts)
n = int(input())
price = list(map(int, input().split()))

# Please write your code here.
min_price = 10 ** 30
best = 0

for p in price:
    if p < min_price:
        min_price = p
    else:
        best = max(best, p - min_price)

print(best)
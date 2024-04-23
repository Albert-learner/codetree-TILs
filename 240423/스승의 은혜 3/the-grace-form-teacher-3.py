n, b = map(int, input().split())
wishes = [tuple(map(int, input().split())) for _ in range(n)]

ans = 0
for i in range(n):
    tmp = [list(wishes[j]) for j in range(n)]

    tmp[i][0] /= 2

    prices = [(tmp[k][0] + tmp[k][1]) for k in range(n)]
    prices.sort()

    student = 0
    cnt = 0

    for x in range(n):
        if cnt + prices[x] > b:
            break
        cnt += prices[x]
        student += 1

    ans = max(ans, student)

print(ans)
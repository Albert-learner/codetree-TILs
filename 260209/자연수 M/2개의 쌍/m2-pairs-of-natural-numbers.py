N = int(input())
pairs = [tuple(map(int, input().split())) for _ in range(N)]

# Please write your code here.
pairs.sort(key = lambda x: x[1])

cnts = [pair[0] for pair in pairs]
vals = [pair[1] for pair in pairs]

i, j = 0, N - 1
ans = 0

while i <= j:
    if i == j:
        if cnts[i] > 0:
            ans = max(ans, vals[i] * 2)
        break

    take = min(cnts[i], cnts[j])
    ans = max(ans, vals[i] + vals[j])

    cnts[i] -= take
    cnts[j] -= take

    if cnts[i] == 0:
        i += 1
    if cnts[j] == 0:
        j -= 1

print(ans)

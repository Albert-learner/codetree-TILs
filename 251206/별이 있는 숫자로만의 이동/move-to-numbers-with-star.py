n, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
L = 2 * n - 1         
offset = n - 1

trans = [[0] * L for _ in range(L)]
for i in range(n):
    for j in range(n):
        u = i + j
        v = i - j + offset
        trans[u][v] = board[i][j]

ps = [[0] * (L + 1) for _ in range(L + 1)]
for i in range(L):
    row_ps = ps[i + 1]
    prev_row_ps = ps[i]
    row_t = trans[i]
    s = 0
    for j in range(L):
        s += row_t[j]
        row_ps[j + 1] = prev_row_ps[j + 1] + s

def rect_sum(u0, v0, u1, v1):
    return (ps[u1 + 1][v1 + 1]
            - ps[u0][v1 + 1]
            - ps[u1 + 1][v0]
            + ps[u0][v0])

ans = 0  

for x in range(n):
    for y in range(n):
        su = x + y
        sv = x - y + offset

        u0 = max(su - k, 0)
        u1 = min(su + k, L - 1)
        v0 = max(sv - k, 0)
        v1 = min(sv + k, L - 1)

        s = rect_sum(u0, v0, u1, v1)
        if s > ans:
            ans = s

print(ans)







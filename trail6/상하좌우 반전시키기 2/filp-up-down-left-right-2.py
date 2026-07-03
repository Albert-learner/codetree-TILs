n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
INF = 10 ** 9
answer = INF

dx = [0, 0, 0, -1, 1]
dy = [0, -1, 1, 0, 0]

def press(b, x, y):
    for k in range(5):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < n and 0 <= ny < m:
            b[nx][ny] ^= 1

for mask in range(1 << m):
    b = [row[:] for row in board]
    cnt = 0

    for j in range(m):
        if (mask >> j) & 1:
            press(b, 0, j)
            cnt += 1

    for i in range(1, n):
        for j in range(m):
            if b[i - 1][j] == 0:
                press(b, i, j)
                cnt += 1

    ok = True
    for j in range(m):
        if b[n - 1][j] == 0:
            ok = False
            break

    if ok:
        answer = min(answer, cnt)

print(answer if answer != INF else -1)
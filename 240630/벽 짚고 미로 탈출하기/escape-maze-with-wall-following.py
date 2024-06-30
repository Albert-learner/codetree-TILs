N = int(input())
x, y = map(lambda x: int(x) - 1, input().split())
board = [list(input()) for _ in range(N)]

def in_range(x, y):
    return 0 <= x < N and 0 <= y < N

def move(board, n, x, y, cur):
    cnts = 0

    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
    for _ in range(4):
        cnts += 1
        mx, my = x + dxs[cur], y + dys[cur]

        if not in_range(mx, my):
            return -1, -1, cur
        elif board[mx][my] == '#':
            cur = (cur + 3) % 4
        elif board[mx][my] == '.':
            return mx, my, cur

    return x, y, cur if cnts == 4 else (-1, -1, cur)

def check(board, n, x, y, cur):
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
    right = (cur + 1) % 4
    mx, my = x + dxs[right], y + dys[right]

    if not in_range(mx, my):
        return True

    return board[mx][my] == '#'

def simulate(board, n, x, y):
    cur, result = 0, 0

    for _ in range(n * n):
        x, y, cur = move(board, n, x, y, cur)
        result += 1

        if x == -1 and y == -1:
            break

        if not check(board, n, x, y, cur):
            cur = (cur + 1) % 4

    return result if result != n * n else -1

result = simulate(board, N, x, y)
print(result)
from collections import deque

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

def get_max_golds(sy, sx, n, m, board):
    max_golds = 0
    visited = [[False] * n for _ in range(n)]
    f_dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    for k in range(n):
        for i in range(n):
            visited[i] = [False] * n
        
        visited[sy][sx] = True
        BFS = deque([(sy, sx, 0)])
        total_golds = 0

        while BFS:
            y, x, side = BFS.popleft()

            if k < side:
                break

            total_golds += board[y][x]
            for dy, dx in f_dirs:
                my, mx = y + dy, x + dx

                if my < 0 or mx < 0 or my >= n or mx >= n:
                    continue

                if visited[my][mx]:
                    continue

                visited[my][mx] = True
                BFS.append((my, mx, side + 1))

        cost = k * k + (k + 1) * (k + 1)
        if cost <= total_golds * m:
            max_golds = max(max_golds, total_golds)

    return max_golds

max_golds = 0
for y in range(N):
    for x in range(N):
        max_golds = max(max_golds, get_max_golds(y, x, N, M, board))

print(max_golds)
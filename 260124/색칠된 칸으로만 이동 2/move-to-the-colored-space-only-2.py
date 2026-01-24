from collections import deque

M, N = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(M)]
colored = [list(map(int, input().split())) for _ in range(M)]

colored_cells = []
minv, maxv = 10**18, -10**18
for r in range(M):
    for c in range(N):
        v = board[r][c]
        if v < minv: minv = v
        if v > maxv: maxv = v
        if colored[r][c] == 1:
            colored_cells.append((r, c))

if len(colored_cells) <= 1:
    print(0)
    exit()

dr = (1, -1, 0, 0)
dc = (0, 0, 1, -1)

def can_connect(D: int) -> bool:
    sr, sc = colored_cells[0]
    visited = [[False] * N for _ in range(M)]
    q = deque([(sr, sc)])
    visited[sr][sc] = True

    while q:
        r, c = q.popleft()
        cur = board[r][c]
        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            if 0 <= nr < M and 0 <= nc < N and not visited[nr][nc]:
                if abs(board[nr][nc] - cur) <= D:
                    visited[nr][nc] = True
                    q.append((nr, nc))

    for r, c in colored_cells:
        if not visited[r][c]:
            return False
    return True

lo, hi = 0, maxv - minv 
while lo < hi:
    mid = (lo + hi) // 2
    if can_connect(mid):
        hi = mid
    else:
        lo = mid + 1

print(lo)

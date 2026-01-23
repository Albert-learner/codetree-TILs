n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
from collections import deque

target = (n ** 2 + 1) // 2

dr, dc = (1, -1, 0, 0), (0, 0, 1, -1)

def can_make(d: int) -> bool:
    visited = [[False] * n for _ in range(n)]
    q = deque()

    for r in range(n):
        for c in range(n):
            if visited[r][c]:
                continue

            visited[r][c] = True
            q.append((r, c))
            cnts = 0

            while q:
                x, y = q.popleft()
                cnts += 1
                if cnts >= target:
                    return True

                cur = board[x][y]
                for k in range(4):
                    nx, ny = x + dr[k], y + dc[k]
                    if 0 <= nx < n and 0 <= ny < n  and not visited[nx][ny]:
                        if abs(board[nx][ny] - cur) <= d:
                            visited[nx][ny] = True
                            q.append((nx, ny))

    return False

lo, hi = -1, 1_000_000
while lo + 1 < hi:
    mid = (lo + hi) // 2
    if can_make(mid):
        hi = mid
    else:
        lo = mid

print(hi)
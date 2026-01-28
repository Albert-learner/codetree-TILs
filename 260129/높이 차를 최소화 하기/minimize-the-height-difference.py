n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
from collections import deque

def can_reach_with_diff(D: int) -> bool:
    start = board[0][0]
    end = board[n - 1][m - 1]

    for low in range(1, 501 - D):
        high = low + D
        if not (low <= start <= high and low <= end <= high):
            continue

        visited = [[False] * m for _ in range(n)]
        q = deque()
        visited[0][0] = True
        q.append((0, 0))

        while q:
            x, y = q.popleft()
            if x == n - 1 and y == m - 1:
                return True

            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                    val = board[nx][ny]
                    if low <= val <= high:
                        visited[nx][ny] = True
                        q.append((nx, ny))

    return False

lo, hi = 0, 499
ans = 499
while lo <= hi:
    mid = (lo + hi) // 2
    if can_reach_with_diff(mid):
        ans = mid
        hi = mid - 1
    else:
        lo = mid + 1

print(ans)
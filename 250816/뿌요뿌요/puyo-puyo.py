n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
import sys
sys.setrecursionlimit(1_000_000)

visited = [[False] * n for _ in range(n)]
result, max_num = 0, 0

def DFS(sx, sy):
    val = grid[sx][sy]
    stack = [(sx, sy)]
    visited[sx][sy] = True
    size = 0

    while stack:
        x, y = stack.pop()
        size += 1
        for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            mx, my = x + dx, y + dy
            if 0 <= mx < n and 0 <= my < n:
                if not visited[mx][my] and grid[mx][my] == val:
                    visited[mx][my] = True
                    stack.append((mx, my))

    return size

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            block_size = DFS(i, j)
            if block_size >= 4:
                result += 1
            if block_size > max_num:
                max_num = block_size

print(result, max_num)
from collections import deque
dq=deque()

def in_range(x,y):
    return 0 <= x < N and 0 <= y < N

N, r, c = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

dq.append((r - 1,c - 1))          #인덱스 보정
max_num = board[r-1][c-1]
bigger_nums = []

while dq:
    x, y = dq.popleft()
    visited[x][y] = True
    bigger_nums.append(board[x][y])

    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        mx = x + dx
        my = y + dy

        if in_range(mx,my) and visited[mx][my] == False and board[mx][my] > max_num:
            max_num = board[mx][my]
            dq.append((mx, my))
            break

print(*bigger_nums)
n = int(input())
num = [list(map(int, input().split())) for _ in range(n)]
move_dir = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())

# Please write your code here.
r -= 1
c -= 1

dirs = [(-1, 0), (-1, 1), (0, 1), (1, 1),
        (1, 0), (1, -1), (0, -1), (-1, -1)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def dfs(x, y):
    """(x,y)에서 시작하여 조건을 만족하며 이동할 수 있는 최대 횟수"""
    d = move_dir[x][y] - 1
    dx, dy = dirs[d]
    best = 0
    # 같은 방향으로 직선상 모든 칸을 훑으며, 현재 수보다 큰 칸들만 후보
    step = 1
    while True:
        nx, ny = x + dx * step, y + dy * step
        if not in_range(nx, ny):
            break
        if num[nx][ny] > num[x][y]:
            best = max(best, 1 + dfs(nx, ny))
        step += 1
    return best

print(dfs(r, c))
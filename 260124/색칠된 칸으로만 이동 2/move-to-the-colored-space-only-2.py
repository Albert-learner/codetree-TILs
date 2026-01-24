from collections import deque

# 변수 선언 및 입력
m, n = tuple(map(int, input().split()))
board = [list(map(int, input().split())) for _ in range(m)]
colored = [list(map(int, input().split())) for _ in range(m)]

dxs = [-1, 0, 1, 0]
dys = [0, -1, 0, 1]

visited = [
    [False for _ in range(n)]
    for _ in range(m)
]

# bfs를 통해 d 이하로 차이 나는 칸만 갈 수 있을 때,
# 갈 수 있는 지점을 전부 구해줍니다.
def bfs(d):
    q = deque()
    q.append((start_x, start_y))
    visited[start_x][start_y] = True

    while q:
        p = q.popleft()

        # 인접한 칸 중 갈 수 있는 칸을 찾아
        # 갈 수 있다면 queue에 넣습니다.
        for (dx, dy) in zip(dxs, dys):
            next_x = p[0] + dx
            next_y = p[1] + dy
            if next_x >= 0 and next_x < m and next_y >= 0 and next_y < n:
                if not visited[next_x][next_y] and abs(board[p[0]][p[1]] - board[next_x][next_y]) <= d:
                    q.append((next_x, next_y))
                    visited[next_x][next_y] = True


# d 이하로 차이 나는 칸만 갈 수 있을 때,
# 모든 색칠된 칸으로 이동할 수 있는지 확인합니다.
def reachable(d):
    # visited 배열을 초기화합니다.
    for i in range(m):
        for j in range(n):
            visited[i][j] = False

    bfs(d)

    # 모든 색칠된 칸으로 이동할 수 있는지 확인합니다.
    for i in range(m):
        for j in range(n):
            if colored[i][j] and not visited[i][j]:
                return False
    return True

for i in range(m):
    for j in range(n):
        # 시작점(색칠된 점 중에서)을 구합니다.
        if colored[i][j]:
            start_x = i
            start_y = j

lo = 0                     # 답이 될 수 있는 가장 작은 숫자 값을 설정합니다.
hi = 1000000000            # 답이 될 수 있는 가장 큰 숫자 값을 설정합니다.
ans = 0                    # 답을 저장합니다.

while lo <= hi:            # [lo, hi]가 유효한 구간이면 계속 수행합니다.
    mid = (lo + hi) // 2   # 가운데 위치를 선택합니다.
    if reachable(mid):     # 결정문제에 대한 답이 Yes라면
        hi = mid - 1       # 왼쪽에 조건을 만족하는 숫자가 더 있을 가능성 때문에 right를 바꿔줍니다.
        ans = mid          # 답의 후보들 중 최댓값을 계속 갱신해줍니다.
    else:
        lo = mid + 1       # 결정문제에 대한 답이 No라면 right를 바꿔줍니다.

# 정답을 출력합니다.
print(ans)

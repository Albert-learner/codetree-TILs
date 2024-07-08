# 입력 처리
t = int(input())

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 격자 안에 있는 범위 탐색
def is_in_range(x, y, n):
    return 0 <= x < n and 0 <= y < n

# 남은 구슬들 세기
def count(test_cases, n):
    cnt = 0
    for x, y, d in test_cases:
        if x != n and y != n:
            cnt += 1
    return cnt

# 격자에서 벗어나는 경우 - 방향을 전환하는 함수
def change_dirt(d):
    return (d + 2) % 4

# 이동하는 함수
def move(x, y, d, n):
    next_x = x + dx[d]
    next_y = y + dy[d]
    if is_in_range(next_x, next_y, n):
        return next_x, next_y, d
    else:
        return x, y, change_dirt(d)

for _ in range(t):
    test_cases = []
    n, m = map(int, input().split())

    for _ in range(m):
        x, y, d = input().split()

        if d == 'R':
            d = 0
        elif d == 'D':
            d = 1
        elif d == 'L':
            d = 2
        elif d == 'U':
            d = 3

        x = int(x) - 1
        y = int(y) - 1
        test_cases.append([x, y, d])

    for _ in range(n * 2):  # 격자의 *2만큼 반복하면 무한히 반복되는게 확정되려나
        visited = [[0 for _ in range(n)] for _ in range(n)]
        conflict_positions = set()

        # 각 구슬에 대해 이동 처리
        for i in range(m):
            x, y, d = test_cases[i]

            if x >= n or y >= n:  # x 또는 y가 n을 넘어가면 깨진 구슬이라는 의미이므로 패스
                continue

            nx, ny, nd = move(x, y, d, n)
            test_cases[i] = [nx, ny, nd]

            visited[nx][ny] += 1

            if visited[nx][ny] > 1:
                conflict_positions.add((nx, ny))

        # 충돌 처리
        if conflict_positions:
            for i in range(m):
                x, y, _ = test_cases[i]
                if (x, y) in conflict_positions:
                    test_cases[i] = [n, n, -1]  # 파괴된 구슬로 설정

    # 결과 출력
    print(count(test_cases, n))
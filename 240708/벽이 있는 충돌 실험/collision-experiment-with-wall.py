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

# # 모범답안 1
# MAX_N = 50

# # 변수 선언 및 입력
# t = int(input())
# n, m = 0, 0
# marbles = []
# marble_cnt = [
#     [0 for _ in range(MAX_N + 1)]
#     for _ in range(MAX_N + 1)
# ]

# # 입력으로 주어진 방향을 정의한 dx, dy에 맞도록
# # 변환하는데 쓰이는 dict를 정의합니다.
# mapper = {
#     'U': 0,
#     'R': 1,
#     'L': 2,
#     'D': 3
# }


# # 해당 위치가 격자 안에 들어와 있는지 확인합니다.
# def in_range(x, y):
#     return 1 <= x and x <= n and 1 <= y and y <= n


# # 해당 구슬이 1초 후에 어떤 위치에서 어떤 방향을 보고 있는지를 구해
# # 그 상태를 반환합니다.
# def move(marble):
#     # 구슬이 벽에 부딪혔을 때의 처리를 간단히 하기 위해
#     # dir 기준 0, 3이 대칭 1, 2가 대칭이 되도록 설정합니다.
#     dxs, dys = [-1, 0, 0, 1], [0, 1, -1, 0]
    
#     x, y, move_dir = marble
    
#     # 바로 앞에 벽이 있는지를 판단합니다.
#     nx, ny = x + dxs[move_dir], y + dys[move_dir]
    
#     # Case 1 : 벽이 없는 경우에는 그대로 한 칸 전진합니다.
#     if in_range(nx, ny):
#         return (nx, ny, move_dir)
#     # Case 2 : 벽이 있는 경우에는 방향을 반대로 틀어줍니다.
#     # 위에서 dx, dy를 move_dir 기준 0, 3이 대칭 1, 2가 대칭이 되도록
#     # 설정해놨기 때문에 간단하게 처리가 가능합니다.
#     else:
#         return (x, y, 3 - move_dir)
    

# # 구슬을 전부 한 번씩 움직여봅니다.
# def move_all():
#     for i, marble in enumerate(marbles):
#         marbles[i] = move(marble)


# # 해당 구슬과 충돌이 일어나는 구슬이 있는지 확인합니다.
# # 이를 위해 자신의 현재 위치에 놓은 구슬의 개수가
# # 자신을 포함하여 2개 이상인지 확인합니다.
# def duplicate_marble_exist(target_idx):
#     target_x, target_y, _ = marbles[target_idx]
    
#     return marble_cnt[target_x][target_y] >= 2
    

# # 충돌이 일어나는 구슬을 전부 지워줍니다.
# def remove_duplicate_marbles():
#     global marbles
    
#     # Step2-1 : 각 구슬의 위치에 count를 증가 시킵니다.
#     for x, y, _ in marbles:
#         marble_cnt[x][y] += 1

#     # Step2-2 : 충돌이 일어나지 않은 구슬만 전부 기록합니다.
#     remaining_marbles = [
#         marble
#         for i, marble in enumerate(marbles)
#         if not duplicate_marble_exist(i)
#     ]
    
#     # Step2-3 : 나중을 위해 각 구슬의 위치에 적어놓은 count 수를 다시 초기화합니다.
#     for x, y, _ in marbles:
#         marble_cnt[x][y] -= 1
    
#     # Step2-4 : 충돌이 일어나지 않은 구슬들로 다시 채워줍니다.
#     marbles = remaining_marbles


# # 조건에 맞춰 시뮬레이션을 진행합니다.
# def simulate():
#     # Step1
#     # 구슬을 전부 한 번씩 움직여봅니다.
#     move_all()
    
#     # Step2
#     # 움직임 이후에 충돌이 일어나는 구슬들을 골라 목록에서 지워줍니다.
#     remove_duplicate_marbles()


# for _ in range(t):
#     # 새로운 테스트 케이스가 시작될때마다 기존에 사용하던 값들을 초기화해줍니다.
#     marbles = []
    
#     # 입력
#     n, m = tuple(map(int, input().split()))
#     for _ in range(m):
#         x, y, d = tuple(input().split())
#         x, y = int(x), int(y)
#         marbles.append((x, y, mapper[d]))
    
#     # 2 * n번 이후에는 충돌이 절대 일어날 수 없으므로
#     # 시뮬레이션을 총 2 * n번 진행합니다.
#     for _ in range(2 * n):
#         simulate()
    
#     # 출력
#     print(len(marbles))

# # 모범답안 2
# BLANK = -1
# COLLIDE = -2

# # 변수 선언 및 입력
# t = int(input())
# n, m = 0, 0
# curr_dir = list()
# next_dir = list()

# # 입력으로 주어진 방향을 정의한 dx, dy에 맞도록
# # 변환하는데 쓰이는 dict를 정의합니다.
# mapper = {
#     'U': 0,
#     'R': 1,
#     'L': 2,
#     'D': 3
# }


# # 해당 위치가 격자 안에 들어와 있는지 확인합니다.
# def in_range(x, y):
#     return 1 <= x and x <= n and 1 <= y and y <= n


# # 해당 위치에 dir 방향을 갖는 구슬이 새롭게 추가되는 경우에 대한
# # 처리를 합니다.
# def update_next_dir(x, y, move_dir):
#     # 빈 곳이었다면 해당 구슬을 넣어주고
#     if next_dir[x][y] == BLANK:
#         next_dir[x][y] = move_dir
#     # 빈 곳이 아니었다면 이미 다른 구슬이 놓여져 있는 것이므로
#     # 충돌 표시를 해줍니다.
#     else:
#         next_dir[x][y] = COLLIDE


# def move(x, y, move_dir):
#     # 구슬이 벽에 부딪혔을 때의 처리를 간단히 하기 위해
#     # dir 기준 0, 3이 대칭 1, 2가 대칭이 되도록 설정합니다.
#     dxs, dys = [-1, 0, 0, 1], [0, 1, -1, 0]
    
#     # 바로 앞에 벽이 있는지를 판단합니다.
#     nx, ny = x + dxs[move_dir], y + dys[move_dir]
    
#     # Case 1 : 벽이 없는 경우에는 그대로 한 칸 전진합니다.
#     # 따라서 그 다음 위치에 같은 방향을 갖는 구슬이 있게 됩니다.
#     if in_range(nx, ny):
#         update_next_dir(nx, ny, move_dir)
        
#     # Case 2 : 벽이 있는 경우에는 방향을 반대로 틀어줍니다.
#     # 따라서 같은 위치에 반대 방향을 갖는 구슬이 있게 됩니다.
#     else:
#         update_next_dir(x, y, 3 - move_dir)   


# # 구슬을 전부 한 번씩 움직여봅니다.
# def move_all():
#     global next_dir
    
#     # 그 다음 각 위치에서의 방향들을 전부 초기화 해놓습니다.
#     next_dir = [
#         [BLANK for _ in range(n + 1)]
#         for _ in range(n + 1)
#     ]
    
#     # (i, j) 위치에 구슬이 있는경우
#     # 움직임을 시도해보고, 그 결과를 전부 next_dir에 기록합니다.
#     for i in range(1, n + 1):
#         for j in range(1, n + 1):
#             if curr_dir[i][j] != BLANK:
#                 move(i, j, curr_dir[i][j])
    
#     # next_dir 값을 다시 curr_dir에 복사합니다.
#     for i in range(1, n + 1):
#         for j in range(1, n + 1):
#             curr_dir[i][j] = next_dir[i][j]


# # 충돌이 일어나는 구슬을 전부 지워줍니다.
# def remove_duplicate_marbles():
#     # 충돌이 일어난 구슬들이 있는 위치만 빈 곳으로 설정하면 됩니다.
#     for i in range(1, n + 1):
#         for j in range(1, n + 1):
#             if curr_dir[i][j] == COLLIDE:
#                 curr_dir[i][j] = BLANK


# # 조건에 맞춰 시뮬레이션을 진행합니다.
# def simulate():
#     # Step1
#     # 구슬을 전부 한 번씩 움직여봅니다.
#     move_all()
    
#     # Step2
#     # 움직임 이후에 충돌이 일어나는 구슬들을 골라 목록에서 지워줍니다.
#     remove_duplicate_marbles()


# for _ in range(t):
#     # 입력
#     n, m = tuple(map(int, input().split()))
    
#     # 새로운 테스트 케이스가 시작될때마다 기존에 사용하던 값들을 초기화해줍니다.
#     curr_dir = [
#         [BLANK for _ in range(n + 1)]
#         for _ in range(n + 1)
#     ]
    
#     for _ in range(m):
#         x, y, d = tuple(input().split())
#         x, y = int(x), int(y)
#         curr_dir[x][y] = mapper[d]
    
#     # 2 * n번 이후에는 충돌이 절대 일어날 수 없으므로
#     # 시뮬레이션을 총 2 * n번 진행합니다.
#     for _ in range(2 * n):
#         simulate()
        
#     marble_cnt = sum([
#         curr_dir[i][j] != BLANK
#         for i in range(1, n + 1)
#         for j in range(1, n + 1)
#     ])
    
#     # 출력
#     print(marble_cnt)
import sys

# 입력
N, T = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

# 선언
dxs = [-1, -1, 0, 1, 1, 1, 0, -1]
dys = [0, 1, 1, 1, 0, -1, -1, -1]

# 격자 안에 있는 범위 탐색
def is_in_range(x, y) :
    return 0 <= x < N and 0 <= y < N

# 교체하기
def Exchange(max_num, num) :
    max_row, max_col = Search_point(max_num)
    row, col = Search_point(num)

    temp = board[max_row][max_col]
    board[max_row][max_col] = board[row][col]
    board[row][col] = temp
    return board

# 8방향 중 최대값 찾기 
def Search_dirt(row, col) :
    max_num = -sys.maxsize
    for dx, dy in zip(dxs, dys) :
        next_x, next_y = row + dx, col + dy

        if is_in_range(next_x, next_y) :
            if board[next_x][next_y] > max_num :
                max_num = board[next_x][next_y]
    return max_num

# 각 값들의 위치(r, c) 찾기 
def Search_point(num) :
    for row in range(N) :
        for col in range(N) :
            if board[row][col] == num :
                return row, col

for turn in range(T) :
    # 1부터 n * n까지의 위치 찾기
    for num in range(1, (N ** 2) + 1) :
        row, col = Search_point(num) # 숫자의 위치찾기
        max_num = Search_dirt(row, col) # 8방향 중 최대값 찾기
        arr = Exchange(max_num, num)

    for row in board:
        print(*row)
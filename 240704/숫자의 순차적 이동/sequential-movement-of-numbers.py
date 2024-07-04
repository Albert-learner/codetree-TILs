import sys

# 입력
n, t = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# 선언
dxs = [-1, -1, 0, 1, 1, 1, 0, -1]
dys = [0, 1, 1, 1, 0, -1, -1, -1]

# 격자 안에 있는 범위 탐색
def is_in_range(x, y) :
    return 0 <= x < n and 0 <= y < n

# 8방향 중 최대값 찾기 
def Search_dirt(row, col) :
    max_num = -sys.maxsize
    for dx, dy in zip(dxs, dys) :
        next_x, next_y = row + dx, col + dy

        if is_in_range(next_x, next_y) :
            if arr[next_x][next_y] > max_num :
                max_num = arr[next_x][next_y]
    return max_num

# 각 값들의 위치(r, c) 찾기 
def Search_point(num) :
    for row in range(n) :
        for col in range(n) :
            if arr[row][col] == num :
                return row, col

# 교체하기
def Exchange(max_num, num, row, col) :
    max_row, max_col = Search_point(max_num)

    temp = arr[max_row][max_col]
    arr[max_row][max_col] = arr[row][col]
    arr[row][col] = temp
    return arr
for turn in range(t) :
    for num in range(1, (n * n) + 1) :
        row, col = Search_point(num) # 숫자의 위치찾기
        max_num = Search_dirt(row, col) # 8방향 중 최대값 찾기
        arr = Exchange(max_num, num, row, col)

    for row in arr:
        print(*row)
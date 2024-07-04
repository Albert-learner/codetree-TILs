def in_range(x, y, n):
    return 0 <= x < n and 0 <= y < n

def swap(arr, x1, y1, x2, y2):
    arr[x1][y1], arr[x2][y2] = arr[x2][y2], arr[x1][y1]

# 주위 8방향 중 가장 큰 값과 교환
def select_max(arr, x, y, n):
    dx = [-1, -1, -1, 0, 1, 1, 1, 0]
    dy = [-1, 0, 1, 1, 1, 0, -1, -1]

    max_x, max_y = -1, -1

    for dir in range(8):
        nx, ny = x + dx[dir], y + dy[dir]
        if not in_range(nx, ny, n):
            continue

        if max_x == -1:
            max_x, max_y = nx, ny

        if arr[max_x][max_y] < arr[nx][ny]:
            max_x, max_y = nx, ny

    if max_x != -1:  # max_x와 max_y가 업데이트 된 경우에만 교환
        swap(arr, x, y, max_x, max_y)

def progress(arr, n, m):
    for turn in range(m):
        num = 1
        # 1이 적힌 칸부터 n*n이 적힌 칸까지 순차적 swap
        while num <= n * n:
            is_done = False
            for i in range(n):
                for j in range(n):
                    if arr[i][j] == num:
                        select_max(arr, i, j, n)
                        is_done = True
                        break
                if is_done:
                    break
            num += 1

def main():
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    progress(arr, n, m)

    for row in arr:
        print(" ".join(map(str, row)))

if __name__ == "__main__":
    main()
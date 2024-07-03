def in_range(x, y, n):
    return 0 <= x < n and 0 <= y < n

def next_pos(x, y, n, arr):
    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]

    max_num = 0
    max_pos = (x, y)

    for dx, dy in zip(dxs, dys):
        next_x, next_y = x + dx, y + dy
        if in_range(next_x, next_y, n) and arr[next_x][next_y] > max_num:
            max_num = arr[next_x][next_y]
            max_pos = (next_x, next_y)

    return max_pos

def simulate(n, count, arr):
    tmp_count = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if count[i][j] == 1:
                x, y = next_pos(i, j, n, arr)
                tmp_count[x][y] += 1
    return tmp_count

def boom(n, count):
    for i in range(n):
        for j in range(n):
            if count[i][j] >= 2:
                count[i][j] = 0
    return count

def main():
    n, m, t = map(int, input().split())

    arr = [
        list(map(int, input().split()))
        for _ in range(n)
    ]

    count = [[0] * n for _ in range(n)]
    for _ in range(m):
        x, y = map(int, input().split())
        count[x - 1][y - 1] = 1

    for _ in range(t):
        count = simulate(n, count, arr)
        count = boom(n, count)

    total_sum = sum(sum(row) for row in count)
    print(total_sum)

if __name__ == "__main__":
    main()
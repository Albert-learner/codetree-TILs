#define MAX_N 100
#define DIR_NUM 5

n = int(input())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]


def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

dxs, dys = [0, 0, 1, 0, -1], [0, 1, 0, -1, 0]


# 1행 i열의 숫자를 반전시킬 수 있는 칸은
# 2행 i열밖에 없습니다. 따라서 1행 i열이 0이라면 2행 i열은
# 반드시 반전되어야만 합니다.
# 그리고 1행 i열이 1이라면 반드시 2행 i열은 반전되지 않아야만 합니다.

# 이렇게 2행의 상태 반전 여부가 확정되면, 그 이후
# 2행 i열의 숫자를 반전시킬 수 있는 칸은
# 3행 i열밖에 없습니다. 따라서 2행의 0과 1에 따라
# 3행의 반전 여부 역시 결정나게 됩니다.

# 이를 반복하면 모든 칸에서 눌러야 할지 안눌러야 할지 결정이 됩니다.

# 현재 위치에서 꼭 눌러야만
# 문제 조건을 만족시킬 수 있다면
# 눌러주고 넘어갑니다.
cnt = 0
for i in range(1, n):
    for j in range(0, n):
        # arr[i - 1][j]가 0이면 누릅니다.
        if arr[i - 1][j] == 0:
            cnt += 1
            for dx, dy in zip(dxs, dys):
                x = i + dx
                y = j + dy

                if in_range(x, y):
                    arr[x][y] = 1 - arr[x][y]


# 만약 결정된 대로 눌렀음에도 n번째 행이 전부 1이 아니라면
# 전부 1로 만드는 것이 불가능한 상황입니다.
possible = True
for elem in arr[n - 1]:
    if elem != 1:
        possible = False

if possible == False:
    print(-1)
else:
    print(cnt)

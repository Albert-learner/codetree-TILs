n = int(input())
arr = [
    list(map(int, input()))
    for _ in range(n)
]


# 뒤에서부터 선택을 진행합니다.
# 현재 위치에서 꼭 눌러야만
# 문제 조건을 만족시킬 수 있다면
# 눌러주고 넘어갑니다.
cnt = 0
for i in range(n - 1, -1, -1):
    for j in range(n - 1, -1, -1):
        # arr[i][j]가 1이면 누릅니다.
        if arr[i][j] == 1:
            cnt += 1
            for k in range(0, i + 1):
                for l in range(0, j + 1):
                    arr[k][l] = 1 - arr[k][l]


print(cnt)

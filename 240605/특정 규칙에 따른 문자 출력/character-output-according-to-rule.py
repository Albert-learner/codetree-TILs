N = int(input())

grid = [[' ' for _ in range(N)] for _ in range(2 * N - 1)]

for i in range(N):
    x, y = 2 * N - 1 - i, i
    for j in range(N):
        nx, ny = x - 1, y
        grid[nx][ny] = '@'
        x, y = nx, ny

for i in range(2 * N - 1):
    for j in range(N):
        print(grid[i][j], end = ' ')
    print()

# # 모범답안
# # 변수 선언 및 입력
# n = int(input())

# # 모양에 맞게 윗쪽 별을 출력합니다.
# for i in range(n):
# 	for _ in range(n - i - 1):
# 		print(" ", end=" ")
# 	for _ in range(i + 1):
# 		print("@", end=" ")
# 	print()

# # 모양에 맞게 아랫쪽 별을 출력합니다.
# for i in range(n - 2, -1, -1):
# 	for _ in range(i+1):
# 		print("@", end=" ")
# 	print()
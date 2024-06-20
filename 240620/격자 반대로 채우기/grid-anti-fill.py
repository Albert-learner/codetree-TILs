N = int(input())
board = [[0] * N for _ in range(N)]

num = 0
if N % 2 == 0:
    for j in range(N - 1, -1, -1):
        if j % 2 == 1:
            for i in range(N - 1, -1, -1):
                num += 1
                board[i][j] = num
        else:
            for i in range(N):
                num += 1
                board[i][j] = num
else:
    for j in range(N - 1, -1, -1):
        if j % 2 == 0:
            for i in range(N - 1, -1, -1):
                num += 1
                board[i][j] = num
        else:
            for i in range(N):
                num += 1
                board[i][j] = num

for row in board:
    print(*row)

# # 모범답안
# # 변수 선언 및 입력
# n = int(input())
# answer = [
#     [0 for _ in range(n)]
#     for _ in range(n)
# ]
# count = 1

# # 격자를 채워줍니다.
# for col in range(n - 1, -1, -1):
#     if (n - 1 - col) % 2 == 0:
#         # 이 케이스에는 아래에서 위로 값을 채워줍니다.
#         for row in range(n - 1, -1, -1):
#             answer[row][col] = count
#             count += 1
#     else:
#         # 이 케이스에는 위에서 아래로 값을 채워줍니다.
#         for row in range(n):
#             answer[row][col] = count
#             count += 1

# # 출력:
# for row in answer:
#     for elem in row:
#         print(elem, end=" ")
#     print()
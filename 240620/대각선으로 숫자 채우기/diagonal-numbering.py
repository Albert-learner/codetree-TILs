N, M = map(int, input().split())
board = [[0] * M for _ in range(N)]

num = 1
ij_sum = 0

while ij_sum <= N * M:
    for i in range(N):
        for j in range(M):
            if i + j == ij_sum:
                board[i][j] = num
                num += 1
            else:
                continue

    ij_sum += 1

for row in board:
    print(*row)

# # 모범답안 1
# # 변수 선언 및 입력
# n, m = tuple(map(int, input().split()))
# answer = [
#     [0 for _ in range(m)]
#     for _ in range(n)
# ]
# count = 1

        
# # Step 1:
# for start_col in range(m):
#     curr_row = 0
#     curr_col = start_col

#     while 0 <= curr_col and curr_row < n:
#         answer[curr_row][curr_col] = count
        
#         # 변수 업데이트
#         curr_row += 1
#         curr_col -= 1
#         count += 1

# # Step 2:
# for start_row in range(1, n):
#     curr_row = start_row
#     curr_col = m - 1

#     while 0 <= curr_col and curr_row < n:
#         answer[curr_row][curr_col] = count
        
#         # 변수 업데이트
#         curr_row += 1
#         curr_col -= 1
#         count += 1

# # 출력:
# for row in range(n):
#     for col in range(m):
#         print(answer[row][col], end = ' ')
#     print()

# # 모범답안 2
# # 변수 선언 및 입력
# n, m = tuple(map(int, input().split()))
# answer = [
#     [0 for _ in range(m)]
#     for _ in range(n)
# ]
# count = 1
        
# # Step 1:
# for start_col in range(m):
#     curr_row = 0
#     curr_col = start_col

#     while 0 <= curr_col and curr_row < n:
#         answer[curr_row][curr_col] = count
        
#         # 변수 업데이트
#         curr_row += 1
#         curr_col -= 1
#         count += 1

# # Step 2:
# for start_row in range(1, n):
#     curr_row = start_row
#     curr_col = m - 1

#     while 0 <= curr_col and curr_row < n:
#         answer[curr_row][curr_col] = count
        
#         # 변수 업데이트
#         curr_row += 1
#         curr_col -= 1
#         count += 1

# # 출력:
# for row in range(n):
#     for col in range(m):
#         print(answer[row][col], end = ' ')
#     print()
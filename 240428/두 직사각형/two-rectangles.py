x1, y1, x2, y2 = map(int, input().split())
a1, b1, a2, b2 = map(int, input().split())

board = [[0] * 101 for _ in range(101)]

for i in range(x1, x2 + 1):
    for j in range(y1, y2 + 1):
        board[i][j] += 1

for i in range(a1, a2 + 1):
    for j in range(b1, b2 + 1):
        board[i][j] += 1

confirm = False
for row in range(len(board)):
    for col in range(len(board[0])):
        if board[row][col] >= 2:
            confirm = True
            break

if confirm:
    print("overlapping")
else:
    print("nonoverlapping")

# # 모범답안
# # 변수 선언 및 입력:
# x1, y1, x2, y2 = tuple(map(int, input().split()))
# a1, b1, a2, b2 = tuple(map(int, input().split()))


# def overlapping(x1, y1, x2, y2, a1, b1, a2, b2):
#     # 겹치지 않는 경우에 대한 처리를 먼저 진행합니다.
#     if x2 < a1 or a2 < x1 or b2 < y1 or y2 < b1:
#         return False
#     # 나머지는 전부 겹치는 경우라고 볼 수 있습니다.
#     else:
#         return True


# # 겹치는지를 확인합니다.
# if overlapping(x1, y1, x2, y2, a1, b1, a2, b2):
#     print("overlapping")
# else:
#     print("nonoverlapping")
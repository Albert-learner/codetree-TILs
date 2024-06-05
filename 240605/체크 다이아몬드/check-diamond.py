N = int(input())

for i in range(N):
    for j in range(N, i + 1, -1):
        print(' ', end = '')
    for j in range(i + 1):
        print("* ", end = '')
    print()

for i in range(1, N):
    for j in range(i):
        print(' ', end = '')
    for j in range(N, i, -1):
        print("* ", end = '')
    print()

# # 모범답안
# # 변수 선언 및 입력
# n = int(input())

# # 모양에 맞게 위쪽 별을 출력합니다.
# for i in range(n):
# 	for _ in range(n - i - 1):
# 		print(" ", end="")
# 	for _ in range(i + 1):
# 		print("* ", end="")
# 	print()

# # 모양에 맞게 아래쪽 별을 출력합니다.
# for i in range(n-2, -1, -1):
# 	for _ in range(n - i - 1):
# 		print(" ", end="")
# 	for _ in range(i + 1):
# 		print("* ", end="")
# 	print()
N = int(input())

for i in range(1, N + 1):
    if i % 2 == 1:
        for j in range(N * i - (N - 1), N * i + 1):
            print(j, end = ' ')
    else:
        for j in range(N * i, N * i - N, -1):
            print(j, end = ' ')
    print()

# # 모범답안
# # 변수 선언 및 입력
# n = int(input())
	
# # 좌우 지그재그로 출력합니다.
# for i in range(n):
# 	for j in range(n):
# 		if i % 2 == 0:
# 			print((i * n) + j + 1, end=" ")
# 		else:
# 			print((i * n) + n - j, end=" ")
# 	print()
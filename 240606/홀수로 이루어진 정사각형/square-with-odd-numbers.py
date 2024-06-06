N = int(input())

for i in range(0, 2 * N, 2):
    for j in range(11, N * 2 - 1 + 11, 2):
        print(i + j, end = ' ')
    print()

# # 모범답안
# # 변수 선언 및 입력
# n = int(input())
	
# # n칸의 정사각형에 올바른 숫자를 출력합니다.
# for i in range(n):
# 	for j in range(n):
# 		print(i * 2 + j * 2 + 11, end=" ")
# 	print()
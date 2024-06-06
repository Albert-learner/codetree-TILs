N = int(input())

total = N + 1
for i in range(1, N + 1):
    init = i
    for j in range(1, N + 1):
        print(init, end = '')
        init = total - init
    print()

# # 모범답안
# # 변수 선언 및 입력
# n = int(input())
	
# # 상하로 반복하여 출력합니다.
# for i in range(n):
# 	for j in range(n):
# 		if j % 2 == 0:
# 			print(i + 1, end="")
# 		else:
# 			print(n - i, end="")
# 	print()
N = int(input())

cnts = 1
for i in range(N):
    for j in range(N):
        print(cnts, end = '')
        cnts += 1
        if cnts > 9:
            cnts = 1
    print()

# # 모범답안
# # 변수 선언 및 입력
# n = int(input())
# cnt = 1
	
# # cnt를 이용해 n칸의 정사각형에 올바른 숫자를 출력합니다.
# for _ in range(n):
# 	for _ in range(n):
# 		print(cnt, end="")
# 		cnt += 1
# 		if cnt == 10:
# 			cnt = 1
# 	print()
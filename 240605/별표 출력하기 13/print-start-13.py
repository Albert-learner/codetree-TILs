# N = int(input())

# plus, minus = 1, N
# for i in range(1, N + 1):
#     if i % 2 == 0:
#         print("* " * plus)
#         plus += 1
#     else:
#         print("* " * minus)
#         minus -= 1

# plus = (N // 2 + 1)
# minus = N // 2

# if N % 2 == 0:
#     for i in range(1, N + 1):
#         if i % 2 == 0:
#             print("* " * plus)
#             plus += 1
#         else:
#             print("* " * minus)
#             minus -= 1
# else:
#     for i in range(1, N + 1):
#         if i % 2 == 0:
#             print("* " * minus)
#             minus -= 1
#         else:
#             print("* " * plus)
#             plus += 1

# 모범답안
# 변수 선언 및 입력
n = int(input())

# i가 홀수인 경우 별을 1 + (i // 2)개, 짝수인 경우 n - (i // 2)개 출력합니다
for i in range(2 * n):
	if i % 2 == 1:
		for _ in range(1 + i // 2):
			print("* ", end="")
	else:
		for _ in range(n - i // 2):
			print("* ", end="")
	print()
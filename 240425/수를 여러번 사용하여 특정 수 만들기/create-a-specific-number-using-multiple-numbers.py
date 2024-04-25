A, B, C = map(int, input().split())

max_result = 0
for i in range(C // A + 1):
    cnt = A * i

    num_b = (C - cnt) // B

    cnt += num_b * B
    max_result = max(max_result, cnt)

print(max_result)

# # 효율적이지 않음
# max_result = 0
# for i in range(1000):
#     if A * i > C:
#         break

#     tmp_result = A * i
#     for j in range(1000):
#         if A * i + B * j > C:
#             max_result = max(max_result, tmp_result + B * (j - 1))
#             break

# print(max_result)

# # 모범답안
# # 변수 선언 및 입력
# a, b, c = tuple(map(int, input().split()))

# ans = 0

# # a를 몇 회 사용할지 전부 시도해 봅니다.
# # 모든 경우의 수에 대해 최대가 되도록 하는 수를 계산합니다.
# for i in range(c // a + 1):
#     # a를 i회 사용합니다.
#     cnt = a * i

#     # 값을 최대로 하기 위해 b를 몇회 사용해야 하는지 계산합니다.
#     num_b = (c - cnt) // b

#     cnt += num_b * b
    
#     ans = max(ans, cnt)

# print(ans)
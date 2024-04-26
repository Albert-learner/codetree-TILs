import sys

N = int(input())
points = [tuple(map(int, input().split())) for _ in range(N)]
x_lst, y_lst = list(list(zip(*points))[0]), list(list(zip(*points))[1])

min_cnts = sys.maxsize
for i in range(101):
    if i % 2 == 1:
        continue

    for j in range(101):
        if j % 2 == 1:
            continue

        n1, n2, n3, n4 = 0, 0, 0, 0
        for k in range(N):
            if x_lst[k] < i and y_lst[k] > j:
                n1 += 1
            elif x_lst[k] > i and y_lst[k] > j:
                n2 += 1
            elif x_lst[k] > i and y_lst[k] < j:
                n3 += 1
            else:
                n4 += 1

        max_cnt = max(n1, n2)
        max_cnt = max(max_cnt, n3)
        max_cnt = max(max_cnt, n4)

        min_cnts = min(min_cnts, max_cnt)

print(min_cnts)

# # 모범답안
# MAX_X = 100

# # 변수 선언 및 입력
# n = int(input())
# points = [
#     tuple(map(int, input().split()))
#     for _ in range(n)
# ]

# ans = 100

# # 모든 직선에 대해 전부 시도해 봅니다.
# for i in range(0, MAX_X + 1, 2):
#     for j in range(0, MAX_X + 1, 2):
#         # x = i, y = j 를 기준으로 나눴을 때의 m을 구합니다.
#         # segment : x = i, y = j를 기준으로 1 ~ 4사분면의 점의 개수
#         segment = [0] * 5

#         for x, y in points:
#             # k번째 점이 몇사분면인지 확인하고 해당 위치의 segment를 1 증가시킵니다.
#             if x > i and y > j:
#                 segment[1] += 1
#             elif x < i and y > j:
#                 segment[2] += 1
#             elif x < i and y < j:
#                 segment[3] += 1
#             else:
#                 segment[4] += 1

#         # x = i, y = j로 나눴을때의 m을 구합니다.
#         cur_m = max(segment)

#         ans = min(ans, cur_m)

# print(ans)
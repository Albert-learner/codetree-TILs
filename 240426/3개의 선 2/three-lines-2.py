N = int(input())
x, y = [], []
xy = [[0] * 11 for _ in range(11)]
cases = ["xxx", "xxy", "xyx", "yxx", "yyy", "yyx", "yxy", "xyy"]

for _ in range(N):
    xi, yi = map(int, input().split())
    x.append(xi)
    y.append(yi)
    xy[xi][yi] = 1

def go(n, chr):
    sum_ = 0
    if chr == 'x':
        for i in range(11):
            sum_ += xy[i][n]
    else:
        for i in range(11):
            sum_ += xy[n][i]

    return sum_

for cse in cases:
    c1, c2, c3 = cse[0], cse[1], cse[2]
    for i in range(6):
        for j in range(6):
            for k in range(6):
                if i == j or j == k or k == i:
                    continue

                sum_ = 0
                sum_ += go(i, c1)
                sum_ += go(j, c2)
                sum_ += go(k, c3)

                if sum_ == N:
                    print(1)
                    exit()

print(0)

# # 모범답안
# MAX_X = 10

# # 변수 선언 및 입력
# n = int(input())
# points = [
#     tuple(map(int, input().split()))
#     for _ in range(n)
# ]

# ans = 0

# # 모든 직선에 대해 전부 시도해 봅니다.
# for i in range(MAX_X + 1):
#     for j in range(MAX_X + 1):
#         for k in range(MAX_X + 1):
#             # success : 직선 3개로 모든 점을 지나게 할 수 있으면 true
#             success = True
#             # x축에 평행한 직선 3개로
#             # 모든 점을 지나게 할 수 있는 경우
#             for x, y in points:
#                 # 해당 점이 직선에 닿으면 넘어갑니다
#                 if x == i or x == j or x == k:
#                     continue
                
#                 success = False
#             if success:
#                 ans = 1

#             # x축에 평행한 직선 2개와 y축에 평행한 직선 1개로
#             # 모든 점을 지나게 할 수 있는 경우
#             success = True
#             for x, y in points:
#                 # 해당 점이 직선에 닿으면 넘어갑니다
#                 if x == i or x == j or y == k:
#                     continue
                
#                 success = False
#             if success:
#                 ans = 1
                
#             # x축에 평행한 직선 1개와 y축에 평행한 직선 2개로
#             # 모든 점을 지나게 할 수 있는 경우
#             success = True
#             for x, y in points:
#                 # 해당 점이 직선에 닿으면 넘어갑니다
#                 if x == i or y == j or y == k:
#                     continue
                
#                 success = False
#             if success:
#                 ans = 1
            
#             # y축에 평행한 직선 3개로
#             # 모든 점을 지나게 할 수 있는 경우
#             success = True
#             for x, y in points:
#                 # 해당 점이 직선에 닿으면 넘어갑니다
#                 if y == i or y == j or y == k:
#                     continue
                
#                 success = False
#             if success:
#                 ans = 1

# print(ans)
# 내 풀이(음수 좌표를 고려해야 함)
N = int(input())
rectangles = [list(map(lambda x: int(x) + 100, input().split())) for _ in range(N)]

total_areas = 0
overlap_areas = (min(list(zip(*rectangles))[2]) - max(list(zip(*rectangles))[0])) * (min(list(zip(*rectangles))[3]) - max(list(zip(*rectangles))[1]))
for x1, y1, x2, y2 in rectangles:
    area = (x2 - x1) * (y2 - y1)
    total_areas += area

total_areas -= overlap_areas
print(total_areas)

# # 남의 풀이
# N = int(input())

# arr = [[0] * 201 for _ in range(201)]
# for _ in range(N):
#     x1, y1, x2, y2 = map(int, input().split())
#     x1 += 100
#     y1 += 100
#     x2 += 100
#     y2 += 100

#     for row in range(x1, x2):
#         for col in range(y1, y2):
#             arr[row][col] = 1

# cnts = 0
# for row in range(len(arr)):
#     for col in range(len(arr[0])):
#         if arr[row][col] == 1:
#             cnts += 1

# print(cnts)
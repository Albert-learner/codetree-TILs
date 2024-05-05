x1, y1, x2, y2 = map(int, input().split())
a1, b1, a2, b2 = map(int, input().split())

min_x, min_y = min(x1, x2, a1, a2), min(y1, y2, b1, b2)
max_x, max_y = max(x1, x2, a1, a2), max(y1, y2, b1, b2)

square_len = max(abs(max_x - min_x), abs(max_y - min_y))
print(square_len ** 2)

# # 모범답안
# # 변수 선언 및 입력:
# x1, y1, x2, y2 = tuple(map(int, input().split()))
# a1, b1, a2, b2 = tuple(map(int, input().split()))

# # 만약 직사각형으로 두 직사각형을 포함시키고자 한다면,
# # 주어진 값들 중 가장 큰 x에서 가장 작은 x를 뺀 길이가 
# # 세로 길이가 되어야 합니다.
# # 마찬가지 이유로 가장 큰 y에서 가장 작은 y를 뺀 길이가
# # 가로 길이가 되어야 합니다.
# width = max(x2, a2) - min(x1, a1)
# height = max(y2, b2) - min(y1, b1)

# # 정사각형으로 위 영역을 포함시키려면,
# # 위 직사각형을 덮을 수는 있어야 합니다.
# # 즉, 한 변의 길이가 직사각형의 가로 세로중 더 긴 쪽 이상이여야 합니다.
# print(max(width, height) * max(width, height))
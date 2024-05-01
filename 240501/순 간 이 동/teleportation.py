A, B, x, y = map(int, input().split())

if A > B:
    A, B = B, A

if x > y:
    x, y = y, x

cases = []
if A == x and B == y:
    cases.append(0)

line = [0] * 101
first_case, second_case, third_case = 0, 0, 0
line[A], line[B] = 1, 2
first_case = abs(B - A)
cases.append(first_case)

second_case = abs(A - x) + abs(B - y)
cases.append(second_case)


third_case = abs(A - y) + abs(B - x)
cases.append(third_case)

print(min(cases))

# # 모범답안
# import sys

# INT_MAX = sys.maxsize

# # 변수 선언 및 입력:
# a, b, x, y = tuple(map(int, input().split()))

# min_dist = INT_MAX

# # Case 1. a -> b 바로 이동
# min_dist = min(min_dist, abs(b - a))

# # Case 2. a -> x -> y -> b 순서로 이동
# min_dist = min(min_dist, abs(x - a) + 0 + abs(b - y))

# # Case 3. a -> y -> x -> b 순서로 이동
# min_dist = min(min_dist, abs(y - a) + 0 + abs(b - x))

# print(min_dist)
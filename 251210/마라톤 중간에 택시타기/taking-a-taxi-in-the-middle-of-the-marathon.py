import sys

INT_MAX = sys.maxsize

# 변수 선언 및 입력:
n = int(input())
x, y = [], []

L, R = [0] * n, [0] * n
ans = INT_MAX

# n개의 점 입력
for _ in range(n):
    given_x, given_y = tuple(map(int, input().split()))
    x.append(given_x)
    y.append(given_y)

# L 배열을 채워줍니다.
# L[i] = 0번부터 i번까지 빠지는 부분 없이
#        순서대로 방문하기 위해
#        이동해야 하는 거리의 합
L[0] = 0
for i in range(1, n):    
    L[i] = L[i - 1] + abs(x[i] - x[i - 1]) + abs(y[i] - y[i - 1])

# R 배열을 채워줍니다.
# R[i] = i번부터 n - 1번까지 빠지는 부분 없이
#        순서대로 방문하기 위해
#        이동해야 하는 거리의 합
R[n - 1] = 0
for i in range(n - 2, -1, -1):
    R[i] = R[i + 1] + abs(x[i + 1] - x[i]) + abs(y[i + 1] - y[i])

# 각 체크포인트 마다
# 건너 뛰었다고 했을 때,
# 가능한 거리 합 중 최솟값을 계산합니다.
for i in range(1, n - 1):
    ans = min(ans, L[i - 1] + R[i + 1] + abs(x[i + 1] - x[i - 1]) + abs(y[i + 1] - y[i - 1]))

print(ans)

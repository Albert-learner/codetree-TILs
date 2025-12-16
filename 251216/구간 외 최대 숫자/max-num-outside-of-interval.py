# 변수 선언 및 입력:
n, q = tuple(map(int, input().split()))
arr = list(map(int, input().split()))
L = [0] * n
R = [0] * n

# L 배열을 채워줍니다.
# L[i] = 0번부터 i번 원소 중 최댓값
L[0] = arr[0]
for i in range(1, n):
    L[i] = max(L[i - 1], arr[i])

# R 배열을 채워줍니다.
# R[i] = i번부터 n - 1번 원소 중 최댓값
R[n - 1] = arr[n - 1]
for i in range(n - 2, -1, -1):
    R[i] = max(R[i + 1], arr[i])

# q개의 질의에 대해
# 구간 [a, b] 외 범위에서의 최댓값을 구합니다.
# 구간 [a, b]외 범위에서의 최댓값은
# L[a - 1], R[b + 1] 중 더 큰 값으로 계산이 가능합니다.
for _ in range(q):
    a, b = tuple(map(int, input().split()))
    a, b = a - 1, b - 1
    print(max(L[a - 1], R[b + 1]))

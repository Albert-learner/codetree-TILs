import sys

INT_MAX = sys.maxsize
MAX_N = 1000
MAX_H = 100

# 변수 선언 및 입력
n = int(input())
k = 17
arr = [
    int(input())
    for _ in range(n)
]

ans = INT_MAX
# 크기가 K인 모든 구간을 잡아
# 해당 구간 안에 들어오게 언덕을 깎고
# 그 비용 중 중 최솟값을 계산합니다.
for i in range(MAX_H):
    # 구간 [i, i + k] 에서의 언덕을 깎는
    # 비용을 계산합니다.
    # i + k보다 높은 언덕은 높이가 i + k가 되게 깎으며
    # i보다 낮은 언덕은 높이가 i가 되게 쌓으면 됩니다.
    cost = 0
    for j in range(n):
        if arr[j] < i:
            cost += (arr[j] - i) * (arr[j] - i)
        if arr[j] > i + k:
            cost += (arr[j] - i - k) * (arr[j] - i - k)

    ans = min(ans, cost);

print(ans)
import sys

INT_MAX = sys.maxsize

# 변수 선언 및 입력:
n = int(input())
arr = list(map(int, input().split()))

prefix_sum = [0] * n

# dp[i][j] : [i, j] 구간에 있는 수들을 전부 하나로 합치기 위해
#            필요한 최소 비용을 기록합니다.
dp = [
    [0] * n
    for _ in range(n)
]


# [i, j] 구간에 있는 수들의 합을 반환합니다.
def get_sum(i, j):
    return prefix_sum[j] - prefix_sum[i] + arr[i]

   
# 누적합을 이용하기 위해 미리 계산을 진행합니다.
prefix_sum[0] = arr[0]
for i in range(1, n):
    prefix_sum[i] = prefix_sum[i - 1] + arr[i]

# 최솟값을 구해야 하므로 
# dp 초기값으로 아주 큰 값을 설정합니다.
for i in range(n):
    for j in range(n):
        dp[i][j] = INT_MAX

# 수가 하나만 남았을 때는 종료되므로
# 추가 비용이 들어가지 않습니다.
# 즉, 구간의 크기가 1인 경우 dp값이 0이 되어야 합니다.
# dp[i][i] = 0이 초기조건이 됩니다.
for i in range(n):
    dp[i][i] = 0

# dp는 미리 구해져 있는 작은 문제를 가지고 큰 문제를 풀어야 하므로
# 이러한 유형의 경우 구간을 점점 넓혀가면서 dp값을 채워야만 합니다. 
# 따라서 구간의 크기를 2부터 n까지 증가하게 미리 정해줍니다.
for gap in range(2, n + 1):
    # 구간의 시작위치 i를 정해줍니다.
    for i in range(n - gap + 1):
        # 구간의 크기와 시작 위치가 정해져 있기에
        # 끝 위치는 자동으로 정해집니다.
        j = i + gap - 1

        # [i, j]가 되기 위해
        # 최종적으로 합쳐지는 두 수가
        # 각각 [i, k], [k + 1, j]로부터 온 결과였을 경우의
        # 최적의 비용을 구해 가능한 경우 중 최솟값을 갱신해줍니다.
        # [i, k]까지 합쳐서 나오는 수는 확실하게 arr[i] + .. + arr[k]이고
        # [k + 1, j]까지 합쳐서 나오는 수는 확시랗게 a[k + 1] + .. + arr[j]이므로
        # 두 수를 합쳤을 때 나오는 추가 비용은 arr[i] + ... + arr[j]입니다.
        # 시간을 줄이기 위해 누적합을 이용하여 O(1)에 계산합니다.
        for k in range(i, j):
            cost = dp[i][k] + dp[k + 1][j] + get_sum(i, j)
            dp[i][j] = min(dp[i][j], cost)

# 모든 수를 합치는 데 필요한 최소 비용을 출력합니다.
print(dp[0][n - 1])

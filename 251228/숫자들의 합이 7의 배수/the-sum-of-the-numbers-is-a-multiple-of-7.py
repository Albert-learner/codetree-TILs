import sys

MOD = 7
INT_MAX = sys.maxsize
INT_MIN = -sys.maxsize

# 변수 선언 및 입력:
n = int(input())
a = [0] + [
    int(input())
    for _ in range(n)
]

# 전처리로 모든 시작부터의 누적합에 대해
# 0 ~ 6 나머지가 되는 최소와 최대 idx를 구해 저장해둘 배열을 선언합니다.
max_idx = [INT_MIN] * MOD
min_idx = [INT_MAX] * MOD

# 나머지가 0일 때에는 앞에 아무 숫자도 없을 때가 최소입니다.
min_idx[0] = max_idx[0] = 0

sum_div7 = 0
for i in range(1, n + 1):
    # 1부터 i번째까지 원소를 더한 값의
    # 7로 나눈 나머지를 sum_div7에 저장합니다.
    sum_div7 += a[i]
    sum_div7 %= 7

    # 7로 나눈 나머지 값들 중
    # 등장 위치의 최솟값과 최댓값을 갱신해줍니다.
    max_idx[sum_div7] = max(max_idx[sum_div7], i)
    min_idx[sum_div7] = min(min_idx[sum_div7], i)
 
ans = 0
for i in range(MOD):
    # 나머지가 i인 누적합의 최대 index에서 최소 index를 빼주면
    # 앞에 나온 숫자들의 합이 7로 나눈 나머지가 i일때의
    # 숫자들의 합이 7의 배수가 되는 최대 구간을 알 수 있습니다.
    ans = max(ans, max_idx[i] - min_idx[i])

# 정답을 출력합니다.
print(ans)

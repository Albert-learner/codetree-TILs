# 변수 선언 및 입력:
n, m, c = tuple(map(int, input().split()))
t = list(map(int, input().split()))


# wait 이하로만 기다릴 수 있을 때,
# 모든 사람을 태우는게 가능한지 여부를 판단합니다.
def isPossible(wait):
    bus = 1
    firstArrival = t[0]
    firstIndex = 0
    for i in range(n):
        # 시작 사람부터 i번째 사람까지 한번에 타지 못하게 되면,
        # i-1번째 사람까지를 한번에 태우고 i번째 사람을 시작 사람으로 갱신합니다.
        if t[i] - firstArrival > wait or i + 1 - firstIndex > c:
            bus += 1
            firstArrival = t[i]
            firstIndex = i
    return bus <= m


t.sort()

lo = 0                     # 답이 될 수 있는 가장 작은 숫자 값을 설정합니다.
hi = 10**9                 # 답이 될 수 있는 가장 큰 숫자 값을 설정합니다.
ans = 10**9                # 답을 저장합니다.

while lo <= hi:            # [lo, hi]가 유효한 구간이면 계속 수행합니다.
    mid = (lo + hi) // 2   # 가운데 위치를 선택합니다.
    if isPossible(mid):    # 결정문제에 대한 답이 Yes라면
        hi = mid - 1       # 왼쪽에 조건을 만족하는 숫자가 더 있을 가능성 때문에 right를 바꿔줍니다.
        ans = min(ans, mid)# 답의 후보들 중 최솟값을 계속 갱신해줍니다.
    else:
        lo = mid + 1       # 결정문제에 대한 답이 No라면 right를 바꿔줍니다.

# 정답을 출력합니다.
print(ans)

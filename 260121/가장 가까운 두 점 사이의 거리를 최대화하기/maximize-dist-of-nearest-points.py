# 변수 선언 및 입력:
n = int(input())
segments = [
    list(map(int, input().split())) 
    for _ in range(n)
]

# 구간을 시작점이 빠른 순으로 정렬합니다.
segments.sort()


def is_possible(mid):
    curr_x, _ = segments[0]            # 최적의 점의 위치를 구해줍니다.
    for x1, x2 in segments[1:]:
        if x2 < curr_x + mid:          # 최소 거리를 더했는데 구간을 벗어난다면
            return False               # 불가능한 경우입니다.
        curr_x = max(curr_x + mid, x1) # 최적의 점의 위치를 갱신합니다.
    
    return True                      # 끝까지 진행했을 때 문제가 없다면 True를 반환합니다.


lo = 1                               # 답이 될 수 있는 가장 작은 숫자 값을 설정합니다.
hi = 10**9                           # 답이 될 수 있는 가장 큰 숫자 값을 설정합니다.
ans = 0                              # 답을 저장합니다.

while lo <= hi:                      # [lo, hi]가 유효한 구간이면 계속 수행합니다.
    mid = (lo + hi) // 2             # 가운데 위치를 선택합니다.

    if is_possible(mid):             # 결정문제에 대한 답이 Yes라면
        lo = mid + 1                 # 오른쪽에 조건을 만족하는 숫자가 더 있을 가능성 때문에 lo를 바꿔줍니다.
        ans = max(ans, mid)          # 답의 후보들 중 최댓값을 계속 갱신해줍니다.
    else:
        hi = mid - 1                 # 결정문제에 대한 답이 No라면 hi를 바꿔줍니다.

# 정답을 출력합니다.
print(ans)

MAX_NUM = 10**18

# 변수 선언 및 입력:
n, m = tuple(map(int, input().split()))
segments = [
    tuple(map(int, input().split()))
    for _ in range(m)
]


# 가장 가까운 두 점 사이의 거리를 dist로 제한 한다고 했을 때
# 점을 n개 놓을 수 있을지를 판단합니다.
def is_possible(dist):
    # 놓을 수 있는 점의 수를 게산합니다.
    # dist가 정해져 있는 이상
    # 최대한 좌측으로 밀착하여 점을 놓아주는 것이 좋습니다.
    cnt = 0
    last_x = -MAX_NUM
    for a, b in segments:
        # 현재 선분에 점을 계속 놓을 수 있을 때까지
        # 점을 추가하고, 마지막으로 놓은 점의 위치를 갱신해줍니다.
        while last_x + dist <= b:
            cnt += 1
            last_x = max(a, last_x + dist)

            if cnt >= n:
                break

    # 놓을 수 있는 점의 개수가 n개 이상이라면 True
    # 아니라면 불가능한 것이므로 False를 반환합니다.
    return cnt >= n


# 선분의 시작점을 기준으로 오름차순 정렬을 진행합니다.
segments.sort()

left = 1                                # 답이 될 수 있는 가장 작은 숫자 값을 설정합니다.
right = MAX_NUM                         # 답이 될 수 있는 가장 큰 숫자 값을 설정합니다.
ans = 0                                 # 답을 저장합니다.

while left <= right:                    # [left, right]가 유효한 구간이면 계속 수행합니다.
    mid = (left + right) // 2           # 가운데 위치를 선택합니다.
    if is_possible(mid):                # 결정문제에 대한 답이 Yes라면
        left = mid + 1                  # 오른쪽에 조건을 만족하는 숫자가 더 있을 가능성 때문에 left를 바꿔줍니다.
        ans = max(ans, mid)             # 답의 후보들 중 최댓값을 계속 갱신해줍니다.
    else:
        right = mid - 1                 # 결정문제에 대한 답이 No라면 right를 바꿔줍니다.

print(ans)

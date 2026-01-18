MAX_NUM = 10**9

# 변수 선언 및 입력:
n, m = tuple(map(int, input().split()))
arr = [
    int(input())
    for _ in range(n)
]


# 가장 인접한 두 물건의 거리를 dist로 한다 했을 때
# 물건을 m개 설치할 수 있을지를 판단합니다.
def is_possible(dist):
    # 설치할 수 있는 물건의 수를 계산합니다.
    # dist가 정해져 있는 이상
    # 최대한 가장 왼쪽부터 설치하는 것이 좋습니다.
    cnt = 1
    last_idx = 0
    for i in range(1, n):
        # 거리가 dist 이상 떨어지게 되는 순간
        # 새로운 물건을 설치하는 것이 최선입니다.
        if arr[i] - arr[last_idx] >= dist:
            # 물건을 하나 더 설치해주고
            # 가장 최근에 놓은 물건의 위치를 
            # 갱신해줍니다.
            cnt += 1
            last_idx = i

    # 설치할 수 있는 물건의 수가 m개 이상이라면 True
    # 아니라면 불가능한 것이므로 False를 반환합니다.
    return cnt >= m


# 물건의 위치를 정렬해줍니다.
arr.sort()

left = 1                          # 답이 될 수 있는 가장 작은 숫자 값을 설정합니다.
right = MAX_NUM                   # 답이 될 수 있는 가장 큰 숫자 값을 설정합니다.
ans = 0                           # 답을 저장합니다.

while left <= right:              # [left, right]가 유효한 구간이면 계속 수행합니다.
    mid = (left + right) // 2     # 가운데 위치를 선택합니다.
    if is_possible(mid):          # 결정문제에 대한 답이 Yes라면
        left = mid + 1            # 오른쪽에 조건을 만족하는 숫자가 더 있을 가능성 때문에 left를 바꿔줍니다.
        ans = max(ans, mid)       # 답의 후보들 중 최댓값을 계속 갱신해줍니다.
    else:        
        right = mid - 1           # 결정문제에 대한 답이 No라면 right를 바꿔줍니다.

print(ans)

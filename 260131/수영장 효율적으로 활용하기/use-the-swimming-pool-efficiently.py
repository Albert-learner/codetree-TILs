MAX_NUM = 10**9

# 변수 선언 및 입력:
n, m = tuple(map(int, input().split()))
arr = list(map(int, input().split()))


# 레인별 사람들의 수영장 이용시간의 합들 중 최댓값을
# limit이라 했을 때
# n명의 사람을 전부 통과시키는 데 
# 필요한 레인 수를 계산하여
# 이 값이 m 이하인지를 확인합니다.
def is_possible(limit):
    # 순서대로 사람들을 통과시킵니다.
    # 이때 현재 몇 번 레인을 쓰고 있는지,
    # 해당 레인에서 수영장 이용시간의 합을 관리합니다.
    lane_num = 1
    sum_of_hours = 0
    for i in range(n):
        # 한 사람의 수영장 이용시간이
        # limit보다 큰 경우는
        # 애초에 불가능하므로
        # 바로 False를 반환합니다.
        if arr[i] > limit:
            return False

        # 합이 limit을 넘는 경우라면
        # 해당 사람을 새로운 레인에 할당시켜줍니다.
        if sum_of_hours + arr[i] > limit:
            lane_num += 1
            sum_of_hours = arr[i]
        # 그렇지 않다면 이용시간의 합을 갱신해줍니다.
        else:
            sum_of_hours += arr[i]

    # n명의 사람이 모두 수영장을 이용하기 위해
    # 필요한 lane의 수가 m개 이하라면 가능한 것이므로 True를,
    # 아니라면 불가능한 것이므로 False를 반환합니다.
    return lane_num <= m


left = 1                      # 답이 될 수 있는 가장 작은 숫자 값을 설정합니다.
right = MAX_NUM               # 답이 될 수 있는 가장 큰 숫자 값을 설정합니다.
ans = MAX_NUM                 # 답을 저장합니다.

while left <= right:          # [left, right]가 유효한 구간이면 계속 수행합니다.
    mid = (left + right) // 2 # 가운데 위치를 선택합니다.
    if is_possible(mid):      # 결정문제에 대한 답이 Yes라면
        right = mid - 1       # 왼쪽에 조건을 만족하는 숫자가 더 있을 가능성 때문에 right를 바꿔줍니다.
        ans = min(ans, mid)   # 답의 후보들 중 최솟값을 계속 갱신해줍니다.
    else:                 
        left = mid + 1        # 결정문제에 대한 답이 No라면 left를 바꿔줍니다.

print(ans)

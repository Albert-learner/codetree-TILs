# 변수 선언 및 입력:
n = int(input())
meetings = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

# 끝나는 시간을 기준으로 정렬합니다.
meetings.sort(key=lambda x: x[1])

# 끝나는 시간이 증가하는 순으로 보며
# 겹치지 않는 경우에 해당하는 회의를
# 전부 선택합니다.

# 가장 최근에 잡힌 회의가 끝난 시간을 기록하며 진행합니다.
last_e, ans = -1, 0
for s, e in meetings:
    # 이전 회의와 겹치지 않는다면
    # 해당 회의를 선택해줍니다. 
    if last_e <= s:
        last_e = e
        ans += 1

print(ans)

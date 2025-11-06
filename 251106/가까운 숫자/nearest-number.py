from sortedcontainers import SortedSet
import sys

INT_MAX = sys.maxsize

# 변수 선언 및 입력:
n = int(input())
queries = list(map(int, input().split()))

s = SortedSet()
ans = INT_MAX

# x = 0 위치에 점을 놓고 시작합니다.
s.add(0)

for x in queries:
    # 가장 근처에 있는 오른쪽 점을 찾습니다.
    idx = s.bisect_right(x)
    # 존재한다면, 거리 중 최솟값을 갱신합니다.
    if idx != len(s):
        ans = min(ans, s[idx] - x)
    
    # 가장 근처에 있는 왼쪽 점을 찾습니다.
    idx -= 1
    # 거리 중 최솟값을 갱신합니다.
    ans = min(ans, x - s[idx])

    # 해당 점을 treeset에 추가합니다.
    s.add(x)
    print(ans)

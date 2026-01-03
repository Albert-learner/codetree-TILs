import sys
from sortedcontainers import SortedSet

n, d = tuple(map(int, input().split()))
point = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

point = [(0, 0)] + sorted(point)

# 변수 선언
point_count = SortedSet()

def get_min():
    if not point_count: return 0
    return point_count[0][0]

def get_max():
    if not point_count: return 0
    return point_count[-1][0]


# 가능한 구간 중 최소 크기를 구합니다.
ans = sys.maxsize

# 구간을 잡아봅니다.
j = 0
for i in range(1, n + 1):
    # y좌표 차가 d가 되기 전까지 계속 진행합니다.
    while j + 1 <= n and get_max() - get_min() < d:
        point_count.add((point[j + 1][1], point[j + 1][0]))
        j += 1

    # 만약 최대한 이동했는데도
    # y좌표 차가 d가 되지 못했다면
    # 탐색을 종료합니다.
    if get_max() - get_min() < d:
        break

    # 현재 구간 [i, j]는 
    # point[i]를 시작점으로 하는
    # 가장 짧은 구간이므로
    # 구간 크기 중 최솟값을 갱신합니다.
    ans = min(ans, point[j][0]-point[i][0])
    
    # 다음 구간으로 넘어가기 전에
    # point[i]에 해당하는 값은 point_count에서 지워줍니다.
    point_count.remove((point[i][1], point[i][0]))

# 만약 불가능하다면
# -1을 답으로 합니다.
if ans == sys.maxsize: print(-1)
else: print(ans)

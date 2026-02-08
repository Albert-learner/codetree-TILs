import heapq

MAX_T = 10000

# 변수 선언 및 입력:
n = int(input())
bombs = []
for _ in range(n):
    score, time_limit = tuple(map(int, input().split()))
    # 시간을 기준으로 정렬해야 하므로
    # time_limit을 첫 번째 자리에 넣어줍니다.
    bombs.append((time_limit, score))


# 폭탄 번호가 주어졌을 때
# 해당 폭탄의 시간제한을 반환합니다.
def get_time_limit(bomb_idx):
    time_limit, _ = bombs[bomb_idx]

    return time_limit


# 폭탄 번호가 주어졌을 때
# 해당 폭탄 해체시 얻게 되는 점수를 반환합니다.
def get_score(bomb_idx):
    _, score = bombs[bomb_idx]
    
    return score


# 시간을 기준으로 오름차순 정렬해줍니다.
bombs.sort()

# MAX_T부터 1까지 보며
# 해당 시간에 해체했을 때 가장 점수를 많이 얻을 수 있는 폭탄을 골라줍니다.
# 이렇게 진행하는 방법이 항상 최선의 답을 구해줌을 이용합니다.
# 이때 가능한 폭탄 중 최대 점수를 갖는 폭탄을 빠르게 골라주기 위해
# 우선순위 큐를 이용합니다.
# 우선순위 큐 이용시 큰 값이 먼저 나오게 하기 위해
# -를 붙여 값을 넣어줘야 함에 유의합니다.
pq = []
bomb_idx = n - 1
ans = 0

for t in range(MAX_T, 0, -1):
    # t초에 해체가 가능한 폭탄들을
    # 전부 우선순위 큐에 담아줍니다.
    while bomb_idx >= 0 and get_time_limit(bomb_idx) >= t:
        heapq.heappush(pq, -get_score(bomb_idx))
        bomb_idx -= 1

    # 현재 시간에 해체 가능한 폭탄이 존재한다면
    # 그 중 가장 높은 점수를 얻을 수 있는 폭탄을 해체해줍니다.
    if pq:
        ans += -heapq.heappop(pq)

print(ans)

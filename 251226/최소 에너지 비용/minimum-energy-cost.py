# 변수 선언 및 입력:
n = int(input())
dist = [0] + [0] + list(map(int, input().split()))
cost = [0] + list(map(int, input().split()))

# i번째 장소로 이제 출발할 때 기준으로
# 지금까지 왔던 장소 중
# 에너지 1을 채우는데 필요한 비용이
# 가장 작은 곳을 전처리로 저장합니다.
min_cost = [0] * (n + 1)
min_cost[2] = cost[1]
for i in range(3, n + 1):
    min_cost[i] = min(min_cost[i - 1], cost[i - 1])

ans = 0
for i in range(1, n + 1):
    # 지금까지 왔던 장소 중 에너지 1을 채우는데 필요한 비용이
    # 가장 작은 곳에서 그만큼의 에너지를 충전합니다.
    ans += min_cost[i] * dist[i]

# 정답을 출력합니다.
print(ans)

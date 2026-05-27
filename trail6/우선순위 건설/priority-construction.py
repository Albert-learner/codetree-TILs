from collections import deque

# 변수 선언 및 입력:
n = int(input())
edges = [[] for _ in range(n + 1)]

# 진입차수를 관리합니다.
indegree = [0] * (n + 1)

# total_times[i] : i번 건물이 완성되기까지 걸리는 최소 시간
total_times = [0] * (n + 1)

# setup_time[i] : i번 건물만 짓는데 걸리는 시간
setup_time = [0] * (n + 1)

# dp[i] : i번 일을 완료하기 위해 필요한 최소 시간을 관리합니다.
dp = [0] * (n + 1)

# 위상정렬을 위한 큐를 관리합니다.
q = deque()

# 인접리스트로 관리합니다.
for i in range(1, n + 1):
    setup_time[i], *nums, _ = list(map(int, input().split()))

    for x in nums:
        y = i
        edges[x].append(y)
        indegree[y] += 1 # 진입차수를 갱신합니다.

# 처음 indegree 값이 0인 곳이 시작점이 됩니다.
# 이 노드들을 queue에 넣어줍니다.
for i in range(1, n + 1):
    if not indegree[i]:
        q.append(i)
        
        # 바로 만들 수 있는 건물들은
        # 완성 시간이 곧 짓는 시간입니다.
        total_times[i] = setup_time[i]

# 위상정렬을 진행합니다.
# queue에 원소가 남아있다면 계속 진행합니다.
while q:
    # 가장 앞에 있는 원소를 뽑아줍니다.
    x = q.popleft()
    
    # x에서 갈 수 있는 모든 곳을 탐색합니다.
    for y in edges[x]:
        # total_times 정보를 갱신합니다.
        if total_times[y] < total_times[x] + setup_time[y]:
            total_times[y] = total_times[x] + setup_time[y]

        # 해당 노드의 indegree를 1만큼 감소시켜줍니다.
        indegree[y] -= 1

        # 비로소 indegree가 0이 되었다면
        # queue에 새로 넣어줍니다.
        if not indegree[y]:
            q.append(y)

# n개의 노드가 각 건물이 완성되기까지
# 걸리는 최소 시간을 차례대로 출력합니다.
for i in range(1, n + 1):
    print(total_times[i])

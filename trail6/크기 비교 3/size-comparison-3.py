import heapq

# 변수 선언 및 입력:
n, m = tuple(map(int, input().split()))
edges = [[] for _ in range(n + 1)]

# 진입차수를 관리합니다.
indegree = [0] * (n + 1)

# 위상정렬을 위한 우선순위 큐를 관리합니다.
pq = []

# 인접리스트로 관리합니다.
for _ in range(m):
    x, y = tuple(map(int, input().split()))

    edges[x].append(y) 
    indegree[y] += 1 # 진입차수를 갱신합니다.

# 처음 indegree 값이 0인 곳이 시작점이 됩니다.
# 이 노드들을 priority queue에 넣어줍니다.
for i in range(1, n + 1):
    if not indegree[i]:
        heapq.heappush(pq, i)

# 위상정렬을 진행합니다.
# priority queue에 원소가 남아있다면 계속 진행합니다.
while pq:
    # 가장 앞에 있는 원소를 뽑아줍니다.
    x = heapq.heappop(pq)
    
    # x값을 출력합니다.
    # 뽑히는 순서가 곧 위상정렬 순서가 됩니다.
    print(x, end=" ")

    # x에서 갈 수 있는 모든 곳을 탐색합니다.
    for y in edges[x]:
        # 해당 노드의 indegree를 1만큼 감소시켜줍니다.
        indegree[y] -= 1

        # 비로소 indegree가 0이 되었다면
        # priority queue에 새로 넣어줍니다.
        if not indegree[y]:
            heapq.heappush(pq, y)

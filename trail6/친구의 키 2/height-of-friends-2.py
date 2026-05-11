from collections import deque

# 변수 선언 및 입력:
n, m = tuple(map(int, input().split()))
edges = [[] for _ in range(n + 1)]

# 진입차수를 관리합니다.
indegree = [0] * (n + 1)

# 위상정렬을 위한 큐를 관리합니다.
q = deque()

# 인접리스트로 관리합니다.
for _ in range(m):
    x, y = tuple(map(int, input().split()))

    edges[x].append(y) 
    indegree[y] += 1 # 진입차수를 갱신합니다.

# 처음 indegree 값이 0인 곳이 시작점이 됩니다.
# 이 노드들을 queue에 넣어줍니다.
for i in range(1, n + 1):
    if not indegree[i]:
        q.append(i)

# 위상정렬을 진행합니다.
# queue에 원소가 남아있다면 계속 진행합니다.
cnt = 0
while q:
    # 가장 앞에 있는 원소를 뽑아줍니다.
    x = q.popleft()
    
    # 큐에서 뽑힌 원소의 수를 세줍니다.
    cnt += 1

    # x에서 갈 수 있는 모든 곳을 탐색합니다.
    for y in edges[x]:
        # 해당 노드의 indegree를 1만큼 감소시켜줍니다.
        indegree[y] -= 1

        # 비로소 indegree가 0이 되었다면
        # queue에 새로 넣어줍니다.
        if not indegree[y]:
            q.append(y)

# 큐에 총 n개의 수가 들어갔다면 사이클 없이 정상적으로 topological sort가 구해졌다는 뜻이므로
# 모순이 없게 됩니다.
if cnt == n:
    print("Consistent")
else:
    print("Inconsistent")

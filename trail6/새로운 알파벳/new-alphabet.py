from collections import deque

MAX_ALPHA = 26

# 변수 선언 및 입력:
n = int(input())
word = [""] * (n + 1)

# 각 단어를 입력받습니다.
for i in range(1, n + 1):
    word[i] = input()

edges = [[] for _ in range(MAX_ALPHA + 1)]

# 진입차수를 관리합니다.
indegree = [0] * (MAX_ALPHA + 1)

# 각 정점을 방문했는지 판단합니다.
visited = [False] * (MAX_ALPHA + 1)

# 위상정렬을 위한 큐를 관리합니다.
q = deque()

# 알파벳을 숫자로 관리합니다.
alpha_to_num = {}
num_to_alpha = [' '] * (MAX_ALPHA + 1)

# 그래프에서 노드의 수를 관리합니다.
N = 0

ans = []
is_inf = False

# 쓰인 알파벳의 개수를 확인합니다.
for i in range(1, n + 1):
    for c in word[i]:
        # x가 지금까지 나오지 않은 알파벳이면 추가합니다.
        if c not in alpha_to_num:
            N += 1
            alpha_to_num[c] = N
            num_to_alpha[N] = c

# 각 단어를 순서대로 보며 알파벳이
# 사전순으로 어떻게 돼야 하는지
# 그래프로 저장합니다.
# 그래프를 인접 리스트로 관리합니다.
for i in range(1, n):
    for j in range(min(len(word[i]), len(word[i + 1]))):
        x, y = word[i][j], word[i + 1][j]

        # 두 알파벳이 다르면
        # x가 y보다 사전순으로 앞섭니다.
        if x != y:
            edges[alpha_to_num[x]].append(alpha_to_num[y])
            indegree[alpha_to_num[y]] += 1 # 진입차수를 갱신합니다.
            break

# 처음 indegree 값이 0인 곳이 루트가 됩니다.
# 이 노드들을 queue에 넣어주고, 정답으로 미리 저장해 놓습니다.
for i in range(1, N + 1):
    if not indegree[i]:
        q.append(i)

# 위상정렬을 진행합니다.
# queue에 원소가 남아있다면 계속 진행합니다.
while q:
    # queue에 여러 값이 들어갔을 경우
    # 가능한 답이 여러개입니다.
    if len(q) > 1:
        is_inf = True
    
    # 가장 앞에 있는 원소를 뽑아줍니다.
    x = q.popleft()

    visited[x] = True
    ans.append(x)

    # x에서 갈 수 있는 모든 곳을 탐색합니다.
    for y in edges[x]:
        # 해당 노드의 indegree를 1만큼 감소시켜줍니다.
        indegree[y] -= 1

        # indegree가 0이 되었다면
        # queue에 새로 넣어줍니다.
        if not indegree[y]:
            q.append(y)

# 모든 노드를 방문했다면 그래프 내에 사이클이 존재하지 않는다는 뜻입니다.
is_cycle = False
for i in range(1, N + 1):
    if not visited[i]: 
        is_cycle = True

if is_cycle:
    # 사이클이 존재한다면
    # 알파벳 순서를 만들어내는 것이
    # 불가능한 상황입니다. -1을 출력합니다.
    print(-1)
elif is_inf:
    # 답이 여러개 존재한다면 inf를 출력합니다.
    print("inf")
else:
    # 올바른 순서가 있을 경우 정답을 출력합니다.
    for num in ans:
        print(num_to_alpha[num], end="")

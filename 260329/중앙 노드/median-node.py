import sys
sys.setrecursionlimit(100000)

# 변수 선언 및 입력:
n, r = tuple(map(int, input().split()))
mid_node = 0
edges = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
tree_size = [0] * (n + 1)
max_size, min_size = 0, n

# n - 1개의 간선 정보를 입력받습니다.
for _ in range(n - 1):
    x, y = tuple(map(int, input().split()))
    
    # 간선 정보를 인접리스트에 넣어줍니다.
    edges[x].append(y)
    edges[y].append(x)


# DFS를 통해 중앙 노드를 판단해줍니다.
def find_min_node(x):
    global mid_node

    # 자식 노드의 개수는 edge의 개수 - 1입니다. (edge중 하나는 반드시 부모 노드와 연결되어 있으므로)
    child = len(edges[x]) - 1

    # 단, 루트 노드 한정으로 부모 노드가 없기 때문에 자식 노드가 1개 더 있습니다.
    if x == r: 
        child += 1

    if child >= 2 and mid_node == 0:
        # 최초로 자식노드가 2개 이상인 노드는 중앙 노드입니다.
        mid_node = x

    if child == 0 and mid_node == 0:
        # 만약 중앙 노드가 없는 상태로 리프 노드로 끝났다면 해당 노드는 중앙 노드입니다.
        mid_node = x

    for y in edges[x]:
        # 이미 방문한 노드는 스킵합니다.
        if visited[y]: 
            continue
        
        visited[y] = True
        find_min_node(y)


# DFS를 통해 각 노드를 루트로 하는 서브트리의 노드의 개수를 계산합니다.
def dfs(x):
    tree_size[x] = 1

    for y in edges[x]:
        # 이미 방문한 노드는 스킵합니다.
        if visited[y]: 
            continue

        visited[y] = True
        dfs(y)

        tree_size[x] += tree_size[y]


# 루트 노드로부터 시작해 DFS를 해 정보들을 저장합니다.
visited[r] = True
find_min_node(r)

# visited 배열을 다시 초기화합니다.
for i in range(1, n + 1): 
    visited[i] = False

# DFS를 통해 각 노드를 루트로 하는 서브트리의 노드의 개수를 계산합니다.
visited[mid_node] = True
dfs(mid_node)

for y in edges[mid_node]:
    max_size = max(max_size, tree_size[y])
    min_size = min(min_size, tree_size[y])

# 중앙노드에서 연결된 자식 노드 중 해당 노드로부터 시작한
# 서브트리의 크기가 가장 큰 값에서 작은 값의 차이를 출력합니다.
print(max_size - min_size)

# 변수 선언 및 입력:
n, m = tuple(map(int, input().split()))

# 번호별 그룹을 관리합니다.
uf = [0] * (n + 1)

# 그룹별 노드 개수를 관리합니다.
sz = [0] * (n + 1)

# 각 그룹을 방문했는지 여부를 기록합니다.
visited = [False] * (n + 1)

group_list = []

# 초기 uf, sz 값을 설정합니다.
for i in range(1, n + 1):
    uf[i] = i
    sz[i] = 1


# x의 대표 번호를 찾아줍니다.
def find(x):
    # x가 루트 노드라면 x값을 반환합니다.
    if uf[x] == x:
        return x
    # x가 루트 노드가 아니라면
    # x의 부모인 uf[x]에서 탐색을 더 진행한 뒤
    # 찾아낸 루트 노드를 uf[x]에 넣어줌과 동시에
    # 해당 노드값을 반환합니다.
    uf[x] = find(uf[x])
    return uf[x]


# x, y가 같은 집합이 되도록 합니다.
def union(x, y):
    # x, y의 대표 번호를 찾은 뒤
    # 연결해줍니다.
    X = find(x)
    Y = find(y)
    if X != Y:
        uf[X] = Y
        sz[Y] += sz[X]


# m개의 간선 정보를 입력받습니다.
for _ in range(m):
    x, y = tuple(map(int, input().split()))

    # 주어진 모든 정점을 연결시킵니다.
    union(x, y)

a, b, k = tuple(map(int, input().split()))
   
A = find(a)
B = find(b)
# 모든 노드의 그룹을 정리합니다.
# B번 노드와도, A번 노드와도 연결되지 않은 그룹들을 ans에 저장합니다.
for i in range(1, n + 1):
    I = find(i)

    # A, B와 같은 그룹이라면 패스합니다.
    if I == A or I == B: 
        continue

    # 이미 선택된 그룹이라면 패스합니다.
    if visited[I]: 
        continue

    # 아직 연결되지 않은 그룹들의 크기를 넣어줍니다.
    visited[I] = True
    group_list.append(sz[I])

# a와 연결될 수 있는 최대 노드의 개수를 구합니다.
sz_a = sz[A]

# 내림차순으로 정렬합니다.
group_list.sort(reverse=True)

# a와 가능한 많은 그룹을 연결시킵니다. 최대 k개까지의 그룹을 연결시킬 수 있습니다.
for i in range(min(k, len(group_list))):
    sz_a += group_list[i]

# 최대 k개까지의 그룹을 연결시킨 후 크기의 총합을 출력합니다.
print(sz_a)

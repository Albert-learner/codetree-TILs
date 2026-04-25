# 변수 선언 및 입력:
n, m = tuple(map(int, input().split()))

uf = [0] * (n + 1)
ab_type = [' '] + list(input().split())

edges = [
    tuple(map(int, input().split()))
    for _ in range(m)
]


def find(x):
    if uf[x] == x:
        return x
    uf[x] = find(uf[x])
    return uf[x]


def union(x, y):
    X, Y = find(x), find(y)
    uf[X] = Y


# cost 순으로 오름차순 정렬을 진행합니다.
edges.sort(key=lambda x: x[2])

# uf 값을 초기값을 적어줍니다.
for i in range(1, n + 1):
    uf[i] = i

# cost가 낮은 간선부터 순서대로 보며
# 아직 두 노드가 연결이 되어있지 않을 경우에만
# 해당 간선을 선택하고 두 노드를 합쳐주면서
# mst를 만들어줍니다.
ans = 0
for x, y, cost in edges:
    # 두 노드의 타입이 같다면 해당 간선은 사용할 수 없습니다.
    if ab_type[x] == ab_type[y]: 
        continue;

    # x, y가 연결되어 있지 않다면
    if find(x) != find(y):
        # 해당 간선은 MST에 속하는 간선이므로
        # 답을 갱신해주고
        # 두 노드를 연결해줍니다.
        ans += cost
        union(x, y)

# 모든 정점이 연결되어있는지를 판단하기 위해
# is_all_connected라는 변수에 관리합니다.
is_all_connected = True
for i in range(2, n + 1):
    x = find(1)
    y = find(i)
    if x != y: 
        is_all_connected = False

# 만약 전부 연결되어있다면 사용한 비용의 합을 출력합니다.
# 그렇지 않다면 -1을 출력합니다.
if is_all_connected:
    print(ans)
else:
    print(-1)

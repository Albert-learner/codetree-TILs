# 변수 선언 및 입력:
n, m = tuple(map(int, input().split()))
a, b = tuple(map(int, input().split()))

# 번호별 그룹을 관리합니다.
uf = [0] * (n + 1)

# 초기 uf 값을 설정합니다.
for i in range(1, n + 1):
    uf[i] = i

# m개의 간선 정보를 입력받습니다.
edges = [
    tuple(map(int, input().split()))
    for _ in range(m)
]


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
    uf[X] = Y

   
# 간선을 만족도가 큰 순으로 정렬한뒤, union find를 진행합니다.
edges.sort(key=lambda x : -x[2])

# 도중 a와 b가 연결되면 그 순간의 간선의 만족도를 출력합니다.
for x, y, d in edges:
    union(x, y)
    A = find(a)
    B = find(b)

    # a와 b가 연결되었다는 것은 
    # 현재 만족도 이상의 간선만으로 연결관계를 만들 수 있었다는 의미이므로
    # 현재 값이 답이 됩니다.
    if A == B:
        print(d)
        break

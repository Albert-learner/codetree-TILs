# 변수 선언 및 입력:
n, m = tuple(map(int, input().split()))

# 번호별 그룹을 관리합니다.
uf = [0] * (n + 1)

# 초기 uf 값을 설정합니다.
for i in range(1, n + 1):
    uf[i] = i


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


# 주어진 간선으로
# 연결관계를 만들어줍니다.
for i in range(1, m + 1):
    a, b = tuple(map(int, input().split()))

    # 만약 합치기 전에 이미 대표 번호가 동일하다면
    # cycle이 발생한 상황입니다.
    if find(a) == find(b):
        print(i)
        quit()

    # a와 b를 합쳐줍니다.
    union(a, b)

print("happy")

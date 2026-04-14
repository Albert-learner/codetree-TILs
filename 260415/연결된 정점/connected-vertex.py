# 변수 선언 및 입력:
n, m = tuple(map(int, input().split()))

# 번호별 그룹을 관리합니다.
uf = [0] * (n + 1)

# 각 유니온 그룹의 사이즈를 관리합니다.
sz = [0] * (n + 1)

# 초기 uf 값을 설정합니다.
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

        # 사이즈를 누적해줍니다.
        sz[Y] += sz[X]


for _ in range(m):
    command = input()
    query = command[0]

    if query == 'x':
        a, b = tuple(map(int, command[2:].split()))

        # 합치는 명령입니다.
        union(a, b)
    else:
        a = int(command[2:])

        # 사이즈를 반환합니다.
        a = find(a)
        print(sz[a])

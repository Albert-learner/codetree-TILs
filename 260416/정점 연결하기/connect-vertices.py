# 변수 선언 및 입력:
n = int(input())

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
for _ in range(n - 2):
    a, b = tuple(map(int, input().split()))

    # 합치는 명령입니다.
    union(a, b)

# n - 2개의 간선을 이었을 시, 그래프는 총 두 개의 컴퍼넌트로 분리됩니다.
# 사전순으로 가장 앞서도록 만들려면, 1번 노드와, 그리고 1번 노드의 컴퍼넌트에 있지 않은
# 가장 작은 노드를 찾으면 됩니다.
for i in range(2, n + 1):
    I = find(i)
    if I != find(1):
        print(1, i)
        break

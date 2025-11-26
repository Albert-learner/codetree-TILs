class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

# 기사들을 관리해줄 배열입니다.
nodes = {}

# 기사들의 번호의 범위가 1 ~ 10억이기 때문에, map으로 기사들의 번호들을 관리해줍니다.
nodeId = {}

# 두 기사들을 연결해줍니다.
def connect(s, e):
    if s is not None:
        s.next = e
    if e is not None:
        e.prev = s

# 해당 기사를 자리에서 없애줍니다.
def pop(u):
    connect(u.prev, u.next)
    u.prev = None
    u.next = None

# 입력
n, m = map(int, input().split())
line = list(map(int, input().split()))

# 원탁이기 때문에 연결 리스트가 원형으로 이어져 있음에 유의합니다.
# 첫번째 기사를 먼저 입력받고, 이후에는 이전 기사와 현재 기사를 연결해줍니다.
knightNum = line[0]

# map의 기사의 번호와 배열의 인덱스를 매칭시켜줍니다.
nodeId[knightNum] = 1
nodes[1] = Node(knightNum)
for i in range(2, n + 1):
    knightNum = line[i - 1]
    nodeId[knightNum] = i
    nodes[i] = Node(knightNum)
    connect(nodes[i - 1], nodes[i])

    # 마지막 기사를 입력받았다면, 첫번째 기사와 마지막 기사를 연결해줍니다.
    if i == n:
        connect(nodes[n], nodes[1])

# 왕이 기사들의 번호를 부를 때마다
# 해당 기사의 왼쪽과 오른쪽에 있는 기사들의 번호를 출력합니다.
for _ in range(m):
    # 기사들의 번호를 입력받아 해당 기사의 배열에서의 인덱스를 찾아 연산을 진행합니다.
    knightNum = int(input())
    print(nodes[nodeId[knightNum]].next.val, nodes[nodeId[knightNum]].prev.val)

    # 이름이 불렸다면 해당 기사를 자리에서 없애줍니다.
    pop(nodes[nodeId[knightNum]])

MAXN = 200000

class Node:
    # 학생들을 나타내는 노드입니다.
    def __init__(self, id):
        # 학생의 번호를 나타냅니다.
        self.id = id
        self.prev = None
        self.next = None


def connect(s, e):
    # 두 학생들을 연결해 줍니다.
    if s is not None:
        s.next = e
    if e is not None:
        e.prev = s


def insert_next_range(s, e, v):
    # 번호가 s부터 e까지의 학생들을 번호가 v인 학생 뒤에 연결해 줍니다.
    next_v = v.next
    connect(v, s)
    connect(e, next_v)


def insert_prev_range(s, e, v):
    # 번호가 s부터 e까지의 학생들을 번호가 v인 학생 앞에 연결해 줍니다.
    connect(v.prev, s)
    connect(e, v)


# 현재까지 줄을 서고 있는 총 학생의 수를 나타냅니다.
node_cnt = 1
# 학생들을 나타내는 노드들을 저장합니다.
nodes = [None] * (MAXN + 2)
nodes[1] = Node(1)

q = int(input())
# q개의 행동을 진행합니다.
for _ in range(q):
    line = list(map(int, input().split()))
    option = line[0]

    if option == 1:
        a, b = line[1], line[2]
        # 다음 줄을 서야 할 학생의 번호는
        # 제일 마지막으로 줄을 세웠던 학생의 번호 + 1 입니다.
        init = node_cnt + 1
        # b명의 학생들을 줄을 세워야하기 때문에 node_cnt를 b만큼 증가시켜줍니다.
        node_cnt += b
        # 학생 번호 init ~ init + b - 1 까지의 학생들을 줄을 먼저 세웁니다.
        for i in range(b):
            nodes[init + i] = Node(init + i)
            if i != 0:
                connect(nodes[init + i - 1], nodes[init + i])
        # 해당 학생들을 번호가 a인 학생 뒤에 연결해 줍니다.
        insert_next_range(nodes[init], nodes[init + b - 1], nodes[a])

    if option == 2:
        a, b = line[1], line[2]
        init = node_cnt + 1
        node_cnt += b
        for i in range(b):
            nodes[init + i] = Node(init + i)
            if i != 0:
                connect(nodes[init + i - 1], nodes[init + i])
        # 해당 학생들을 번호가 a인 학생 앞에 연결해 줍니다.
        insert_prev_range(nodes[init], nodes[init + b - 1], nodes[a])

    if option == 3:
        a = line[1]
        # 문제의 조건 대로 출력을 진행합니다.
        if nodes[a].prev is None or nodes[a].next is None:
            print(-1)
        else:
            print(nodes[a].prev.id, nodes[a].next.id)

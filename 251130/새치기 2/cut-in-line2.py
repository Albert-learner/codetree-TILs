class Node:
    # 사람들을 나타내는 노드입니다.
    def __init__(self, name):
        # 사람의 번호를 나타냅니다.
        self.name = name
        self.prev = None
        self.next = None

def connect(s, e):
    # 두 사람을 연결합니다.
    if s is not None:
        s.next = e
    if e is not None:
        e.prev = s

def pop(node):
    # i번 사람을 집에 보냅니다.
    l = lineNum[personId[node.name]]
    # i번 사람이 어느 줄에도 서있지 않다면 아무것도 하지 않습니다.
    if l == 0:
        return

    # i번 사람이 줄의 시작이었다면 줄의 시작을 다음 사람으로 바꿉니다.
    if head[l] == node:
        head[l] = head[l].next
    # i번 사람이 줄의 끝이었다면 줄의 끝을 이전 사람으로 바꿉니다.
    if tail[l] == node:
        tail[l] = tail[l].prev

    # i번 사람을 줄에서 뺍니다.
    if node.prev is not None:
        node.prev.next = node.next
    if node.next is not None:
        node.next.prev = node.prev

    # i번 사람이 어느 줄에도 서있지 않다고 표시합니다.
    lineNum[personId[node.name]] = 0
    node.next = node.prev = None

def insert_front(a, b):
    # a번 사람을 b번 사람 앞에 서게 합니다.
    line_num_b = lineNum[personId[b.name]]
    if head[line_num_b] == b:
        head[line_num_b] = a
    pop(a)
    connect(b.prev, a)
    connect(a, b)
    lineNum[personId[a.name]] = line_num_b

def pop_range_and_insert_prev(a, b, c):
    # a번 사람부터 b번 사람까지를 c번 사람 앞에 이동합니다.
    line_num_a = lineNum[personId[a.name]]
    line_num_c = lineNum[personId[c.name]]

    if head[line_num_a] == a:
        head[line_num_a] = b.next
    if tail[line_num_a] == b:
        tail[line_num_a] = a.prev

    connect(a.prev, b.next)

    if head[line_num_c] == c:
        connect(b, c)
        head[line_num_c] = a
    else:
        connect(c.prev, a)
        connect(b, c)

    cur = a
    while cur != b:
        lineNum[personId[cur.name]] = line_num_c
        cur = cur.next
    lineNum[personId[cur.name]] = line_num_c

def print_line(l):
    # 해당 줄을 전부 출력합니다.
    cur = head[l]
    if cur is None:
        print(-1)
        return

    while cur is not None:
        print(cur.name, end=" ")
        cur = cur.next
    print()

# 사람들을 나타내는 노드들을 저장합니다.
nodes = {}

# 각 줄의 시작과 끝을 나타냅니다.
head = {}
tail = {}

# 각 사람이 몇 번 줄에 서있는지 나타냅니다.
lineNum = {}

# 각 사람의 이름들을 번호로 바꿔줍니다.
personId = {}

# 입력
n, m, q = map(int, input().split())

# m 개의 줄을 입력 받습니다.
personNum = 1
x = list(input().split())
for i in range(1, m + 1):
    for j in range(n // m):
        t = x[personNum - 1]
        personId[t] = personNum
        lineNum[personNum] = i

        if j == 0:
            tail[i] = head[i] = nodes[personNum] = Node(t)
        else:
            nodes[personNum] = Node(t)
            connect(tail[i], nodes[personNum])
            tail[i] = nodes[personNum]

        personNum += 1

# q 개의 문자대로 시뮬레이션을 진행합니다.
for _ in range(q):
    line = list(input().split())
    option = int(line[0])

    if option == 1:
        x, y = line[1], line[2]
        a, b = personId[x], personId[y]
        insert_front(nodes[a], nodes[b])
    elif option == 2:
        x = line[1]
        a = personId[x]
        pop(nodes[a])
    elif option == 3:
        x, y, z = line[1], line[2], line[3]
        a, b, c = personId[x], personId[y], personId[z]
        pop_range_and_insert_prev(nodes[a], nodes[b], nodes[c])

# 출력
for i in range(1, m + 1):
    print_line(i)

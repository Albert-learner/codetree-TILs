N = int(input())
Q = int(input())

type_arr = []
i_arr = []
j_arr = []

for _ in range(Q):
    query = list(map(int, input().split()))
    type_arr.append(query[0])
    i_arr.append(query[1])
    if query[0] in [2, 3]:
        j_arr.append(query[2])
    else:
        j_arr.append(0)

# Please write your code here.
prev = [0] * (N + 1)
next = [0] * (N + 1)

out = []

for q in range(Q):
    t = type_arr[q]
    i = i_arr[q]
    j = j_arr[q]

    if t == 1:
        # 1 i : i번 노드를 그 노드가 속해 있던 연결 리스트에서 분리 (단일 노드로)
        pi = prev[i]
        ni = next[i]

        if pi != 0:
            next[pi] = ni
        if ni != 0:
            prev[ni] = pi

        prev[i] = 0
        next[i] = 0

    elif t == 2:
        # 2 i j : 단일 노드인 j번 노드를 i번 노드 "앞"에 삽입
        # j는 항상 prev[j] == 0, next[j] == 0 이라고 가정 가능
        pi = prev[i]

        prev[j] = pi
        next[j] = i
        prev[i] = j
        if pi != 0:
            next[pi] = j

    elif t == 3:
        # 3 i j : 단일 노드인 j번 노드를 i번 노드 "뒤"에 삽입
        ni = next[i]

        next[j] = ni
        prev[j] = i
        next[i] = j
        if ni != 0:
            prev[ni] = j

    elif t == 4:
        # 4 i : i번 노드의 이전/다음 노드 번호 출력
        out.append(f"{prev[i]} {next[i]}")

# 중간 쿼리들에 대한 출력
print("\n".join(out))

# 마지막에 1번부터 N번까지 각 노드의 "다음 노드" 번호 출력
print(" ".join(str(next[i]) for i in range(1, N + 1)))
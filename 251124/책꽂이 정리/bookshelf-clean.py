import sys
input = sys.stdin.readline

N, K = map(int, input().split())
Q = int(input())
type_arr = []
i_arr = []
j_arr = []
for _ in range(Q):
    t, x, y = map(int, input().split())
    type_arr.append(t)
    i_arr.append(x)
    j_arr.append(y)

# prev[x], next[x] : 책 x의 앞/뒤에 있는 책 번호 (없으면 0)
prev = [0] * (N + 1)
next = [0] * (N + 1)

# 각 책꽂이의 맨 앞/맨 뒤 책 번호, 그리고 책 개수
head = [0] * (K + 1)
tail = [0] * (K + 1)
size = [0] * (K + 1)

# 초기 상태: 모든 책 1..N이 1번 책꽂이에 순서대로
if N > 0:
    head[1] = 1
    tail[1] = N
    size[1] = N
    for x in range(1, N + 1):
        if x > 1:
            prev[x] = x - 1
        if x < N:
            next[x] = x + 1


for q in range(Q):
    t = type_arr[q]
    i = i_arr[q]
    j = j_arr[q]

    if t == 1:
        # 1 i j : i의 맨 앞 책을 j의 맨 뒤로
        if size[i] == 0:
            continue
        book = head[i]

        # i에서 맨 앞 제거
        new_head = next[book]
        head[i] = new_head
        if new_head != 0:
            prev[new_head] = 0
        else:
            tail[i] = 0
        next[book] = 0
        prev[book] = 0
        size[i] -= 1

        # j의 맨 뒤에 붙이기
        if size[j] == 0:
            head[j] = tail[j] = book
        else:
            old_tail = tail[j]
            next[old_tail] = book
            prev[book] = old_tail
            tail[j] = book
        size[j] += 1

    elif t == 2:
        # 2 i j : i의 맨 뒤 책을 j의 맨 앞으로
        if size[i] == 0:
            continue
        book = tail[i]

        # i에서 맨 뒤 제거
        new_tail = prev[book]
        tail[i] = new_tail
        if new_tail != 0:
            next[new_tail] = 0
        else:
            head[i] = 0
        prev[book] = 0
        next[book] = 0
        size[i] -= 1

        # j의 맨 앞에 붙이기
        if size[j] == 0:
            head[j] = tail[j] = book
        else:
            old_head = head[j]
            prev[old_head] = book
            next[book] = old_head
            head[j] = book
        size[j] += 1

    elif t == 3:
        # 3 i j : i의 책들을 모두 j의 맨 앞으로 (순서 유지)
        if i == j or size[i] == 0:
            continue

        hi, ti = head[i], tail[i]
        hj, tj = head[j], tail[j]

        if size[j] == 0:
            # j가 비어 있으면 그냥 통째로 옮김
            head[j], tail[j] = hi, ti
        else:
            # i 리스트를 j 리스트의 앞에 붙이기: [i..] + [j..]
            prev[hj] = ti
            next[ti] = hj
            head[j] = hi

        # i는 비워진다
        head[i] = tail[i] = 0
        size[j] += size[i]
        size[i] = 0

    elif t == 4:
        # 4 i j : i의 책들을 모두 j의 맨 뒤로 (순서 유지)
        if i == j or size[i] == 0:
            continue

        hi, ti = head[i], tail[i]
        hj, tj = head[j], tail[j]

        if size[j] == 0:
            # j가 비어 있으면 그냥 통째로 옮김
            head[j], tail[j] = hi, ti
        else:
            # j 리스트 뒤에 i 리스트 붙이기: [j..] + [i..]
            next[tj] = hi
            prev[hi] = tj
            tail[j] = ti

        # i는 비워진다
        head[i] = tail[i] = 0
        size[j] += size[i]
        size[i] = 0

# 최종 출력
out_lines = []
for shelf in range(1, K + 1):
    cnt = size[shelf]
    if cnt == 0:
        out_lines.append("0")
    else:
        books = []
        cur = head[shelf]
        while cur != 0:
            books.append(str(cur))
            cur = next[cur]
        out_lines.append(str(cnt) + " " + " ".join(books))

print("\n".join(out_lines))

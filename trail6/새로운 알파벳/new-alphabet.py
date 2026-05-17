n = int(input())
words = [input() for _ in range(n)]

# Please write your code here.
from collections import deque

used = set()
for word in words:
    for ch in word:
        used.add(ch)

used = sorted(used)

graph = {ch: set() for ch in used}
indegree = {ch: 0 for ch in used}

possible = True
for i in range(n - 1):
    w1 = words[i]
    w2 = words[i + 1]

    min_len = min(len(w1), len(w2))
    found = False

    for j in range(min_len):
        if w1[j] != w2[j]:
            a = w1[j]
            b = w2[j]

            if b not in graph[a]:
                graph[a].add(b)
                indegree[b] += 1

            found = True
            break

    if not found and len(w1) > len(w2):
        possible = False
        break


if not possible:
    print(-1)
else:
    q = deque()

    for ch in used:
        if indegree[ch] == 0:
            q.append(ch)

    answer = []
    multiple = False

    while q:
        if len(q) >= 2:
            multiple = True

        cur = q.popleft()
        answer.append(cur)

        for nxt in graph[cur]:
            indegree[nxt] -= 1

            if indegree[nxt] == 0:
                q.append(nxt)

    if len(answer) != len(used):
        print(-1)
    elif multiple:
        print("inf")
    else:
        print("".join(answer))
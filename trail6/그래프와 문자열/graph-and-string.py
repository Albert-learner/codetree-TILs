n, S = input().split()
n = int(n)

edges = []
for _ in range(n - 1):
    a, b, c = input().split()
    edges.append((int(a), int(b), c))

# Please write your code here.
L = len(S)
pi = [0] * L

j = 0
for i in range(1, L):
    while j > 0 and S[i] != S[j]:
        j = pi[j - 1]

    if S[i] == S[j]:
        j += 1
        pi[i] = j

graph = [[] for _ in range(n + 1)]
for a, b, c in edges:
    graph[a].append((b, c))

answer = 0
stack = [(1, 0)]
while stack:
    cur, matched = stack.pop()

    for nxt, ch in graph[cur]:
        now = matched

        while now > 0 and ch != S[now]:
            now = pi[now - 1]

        if ch == S[now]:
            now += 1

        if now == L:
            answer += 1
            now = pi[now - 1]

        stack.append((nxt, now))

print(answer)
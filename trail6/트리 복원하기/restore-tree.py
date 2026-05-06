n = int(input())
dist = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
answer = []

for a in range(n):
    for b in range(a + 1, n):
        direct = True

        for k in range(n):
            if k == a or k == b:
                continue

            if dist[a][b] == dist[a][k] + dist[k][b]:
                direct = False
                break

        if direct:
            answer.append((a + 1, b + 1, dist[a][b]))

answer.sort()

for a, b, w in answer:
    print(a, b, w)
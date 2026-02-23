n, a, b = map(int, input().split())
grid = [list(input().strip()) for _ in range(n)]

# Please write your code here.
import heapq

INF = 10 ** 30
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def dijkstra(sr, sc):
    dist = [[INF] * n for _ in range(n)]
    dist[sr][sc] = 0
    pq = [(0, sr, sc)]
    
    while pq:
        d, r, c = heapq.heappop(pq)
        if d != dist[r][c]:
            continue
        
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n:
                w = a if grid[r][c] == grid[nr][nc] else b
                nd = d + w
                if nd < dist[nr][nc]:
                    dist[nr][nc] = nd
                    heapq.heappush(pq, (nd, nr, nc))

    mx = 0
    for i in range(n):
        row_max = max(dist[i])
        if row_max > mx:
            mx = row_max
    return mx

answer = 0
for i in range(n):
    for j in range(n):
        answer = max(answer, dijkstra(i, j))

print(answer)
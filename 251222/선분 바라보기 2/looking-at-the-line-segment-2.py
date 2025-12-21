n = int(input())
y, x1, x2 = [], [], []
for _ in range(n):
    yi, x1i, x2i = map(int, input().split())
    y.append(yi)
    x1.append(x1i)
    x2.append(x2i)

# Please write your code here.
import heapq

events = []
for i in range(n):
    events.append((x1[i], 1, i))
    events.append((x2[i], 0, i))

events.sort(key=lambda t: (t[0], t[1]))

active = [False] * n
heap = []  
visible = set()

m = len(events)
for idx in range(m):
    x, typ, sid = events[idx]

    if typ == 0:
        active[sid] = False
    else:    
        active[sid] = True
        heapq.heappush(heap, (y[sid], sid))

    next_x = events[idx + 1][0] if idx + 1 < m else None
    if next_x is not None and next_x > x:
        while heap and not active[heap[0][1]]:
            heapq.heappop(heap)
        if heap:
            visible.add(heap[0][1])

print(len(visible))
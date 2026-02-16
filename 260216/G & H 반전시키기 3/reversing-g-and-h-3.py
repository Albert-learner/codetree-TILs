N = int(input())
a = input()
b = input()

# Please write your code here.
from collections import deque

diff = [0] * (N + 3)
for i in range(N):
    diff[i] = 1 if a[i] != b[i] else 0

gens = [
    0b0001,  
    0b0011,  
    0b0111, 
    0b1111,  
]

INF = 10**15
cost = [INF] * 16
cost[0] = 0
q = deque([0])
while q:
    cur = q.popleft()
    for g in gens:
        nxt = cur ^ g
        if cost[nxt] > cost[cur] + 1:
            cost[nxt] = cost[cur] + 1
            q.append(nxt)

dp = [INF] * 8
start_state = (diff[0] << 0) | (diff[1] << 1) | (diff[2] << 2)
dp[start_state] = 0

for i in range(N):
    ndp = [INF] * 8
    next_bit = diff[i + 3]  
    for state in range(8):
        if dp[state] == INF:
            continue

        window = state | (next_bit << 3)

        for p in range(16):
            w2 = window ^ p
            if (w2 & 1) != 0:
                continue

            new_state = (w2 >> 1) & 0b111 
            ndp[new_state] = min(ndp[new_state], dp[state] + cost[p])
    dp = ndp

ans = dp[0]
print(ans if ans < INF else -1)


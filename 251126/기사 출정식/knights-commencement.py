N, M = map(int, input().split())
knights = list(map(int, input().split()))
calls = [int(input()) for _ in range(M)]

# Please write your code here.
pos = {knights[i]: i for i in range(N)}

prev = [0] * N
next = [0] * N

for i in range(N):
    prev[i] = (i + 1) % N
    next[i] = (i - 1 + N) % N

out = []
for x in calls:
    idx = pos[x]

    left_idx = prev[idx]
    right_idx = next[idx]

    out.append(f"{knights[left_idx]} {knights[right_idx]}")

    L = prev[idx]
    R = next[idx]
    next[L] = R
    prev[R] = L

print("\n".join(out))
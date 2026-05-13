n, m = map(int, input().split())

a = []
k = []
parts_needed = []

for _ in range(m):
    ai, ki = map(int, input().split())
    a.append(ai)
    k.append(ki)
    parts_needed.append(list(map(int, input().split())))

parts = int(input())
current_parts = list(map(int, input().split()))

# Please write your code here.
from collections import deque

have = [False] * (n + 1)

recipes_by_part = [[] for _ in range(n + 1)]

remain = k[:]

make_cnt = [0] * (n + 1)
satisfied_cnt = [0] * (n + 1)

for i in range(m):
    make_cnt[a[i]] += 1

    for p in parts_needed[i]:
        recipes_by_part[p].append(i)

q = deque()

for p in current_parts:
    if not have[p]:
        have[p] = True
        q.append(p)

while q:
    cur = q.popleft()

    for recipe_idx in recipes_by_part[cur]:
        remain[recipe_idx] -= 1

        if remain[recipe_idx] == 0:
            made = a[recipe_idx]
            satisfied_cnt[made] += 1

            if not have[made] and satisfied_cnt[made] == make_cnt[made]:
                have[made] = True
                q.append(made)

answer = [i for i in range(1, n + 1) if have[i]]

print(len(answer))
print(*answer)
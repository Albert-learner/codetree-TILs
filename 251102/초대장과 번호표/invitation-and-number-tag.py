N, G = map(int, input().split())

group = []
group_size = []

for _ in range(G):
    nums = list(map(int, input().split()))
    group_size.append(nums[0])
    group.append(nums[1:])

# Please write your code here.
from collections import deque

person_groups = [[] for _ in range(N + 1)]
for gi, members in enumerate(group):
    for x in members:
        person_groups[x].append(gi)

invited = [False] * (N + 1)
cnt = [0] * G

q = deque()
invited[1] = True
q.append(1)

while q:
    p = q.popleft()
    for gi in person_groups[p]:
        cnt[gi] += 1
        if cnt[gi] == group_size[gi] - 1:
            missing = None
            for x in group[gi]:
                if not invited[x]:
                    missing = x
                    break
            if missing is not None and not invited[missing]:
                invited[missing] = True
                q.append(missing)

print(sum(invited))
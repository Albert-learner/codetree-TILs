n, m = map(int, input().split())
a_chairs = list(map(int, input().split()))

# Please write your code here.
from sortedcontainers import SortedSet

a_chairs = [-ac for ac in a_chairs]
sset = SortedSet([-i for i in range(1, m + 1)])

answer = 0
for ac in a_chairs:
    idx = sset.bisect_left(ac)
    if idx == len(sset):
        break

    answer += 1
    sset.remove(sset[idx])

print(answer)

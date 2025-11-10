n, m = map(int, input().split())
nums = list(map(int, input().split()))

# Please write your code here.
from sortedcontainers import SortedSet

s_num = SortedSet()
s_len = SortedSet()

s_num.add(-1)
s_num.add(n + 1)

s_len.add((-(n + 1), -1, n + 1))

for num in nums:
    s_num.add(num)

    z = s_num[s_num.bisect_right(num)]
    x = s_num[s_num.bisect_left(num) - 1]

    s_len.remove((
        -(z - x - 1), x, z
    ))
    s_len.add((
        -(num - x - 1), x, num
    ))
    s_len.add((
        -(z - num - 1), num, z
    ))

    best_length, _, _ = s_len[0]
    print(-best_length)
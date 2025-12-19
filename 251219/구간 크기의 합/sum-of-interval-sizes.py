n = int(input())
intervals = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
intervals.sort()

total = 0
cur_l, cur_r = intervals[0]

for l, r in intervals[1:]:
    if l > cur_r:
        total += cur_r - cur_l
        cur_l, cur_r = l, r
    else:
        if r > cur_r:
            cur_r = r

total += cur_r - cur_l

print(total)
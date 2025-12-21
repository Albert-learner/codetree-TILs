n = int(input())
intervals = [tuple(map(int, input().split())) for _ in range(n)]
a, b = zip(*intervals)
a_lst, b_lst = list(a), list(b)

# Please write your code here.
intervals.sort()

total_left, total_right = 0, 0
cur_l, cur_r = intervals[0]

for l, r in intervals[1:]:
    if l > cur_r:
        total_left += cur_r - cur_l
        cur_l, cur_r = l, r
    else:
        if r > cur_r:
            cur_r = r

total_right += cur_r - cur_l
print(max(total_left, total_right))

N = int(input())
chkpnts = [list(map(int, input().split())) for _ in range(N)]

start, end = chkpnts[0], chkpnts[-1]
mid_chkpnts = chkpnts[1:-1]

answer = 0
diffs_lst = []
for x, y in mid_chkpnts:
    st_diff = int(abs(start[0] - x)) + int(abs(start[1] - y))
    ed_diff = int(abs(end[0] - x)) + int(abs(end[1] - y))

    diffs_lst.append([st_diff, ed_diff])

diffs_lst = sorted(diffs_lst, key = lambda x: sum(x))
print(sum(diffs_lst[0]))
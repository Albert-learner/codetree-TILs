N = int(input())
areas_lst = [list(map(int, input().split())) for _ in range(N)]

start_lst = list(zip(*areas_lst))[0]
offset = min(sorted(start_lst)) if min(sorted(start_lst)) < 0 else 0
max_len = max(list(zip(*areas_lst))[1])

checked = [0] * max_len
for start, end in areas_lst:
    start += offset
    end += offset

    for idx in range(start, end):
        checked[idx] += 1

print(max(checked))
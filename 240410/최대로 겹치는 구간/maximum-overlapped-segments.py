N = int(input())
areas_lst = [list(map(int, input().split())) for _ in range(N)]

max_len = max(list(zip(*areas_lst))[-1])
checked = [0] * max_len

for start, end in areas_lst:
    for idx in range(start, end):
        checked[idx] += 1

print(max(checked))
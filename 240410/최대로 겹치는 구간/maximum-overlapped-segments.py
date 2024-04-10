N = int(input())
lines_lst = [list(map(int, input().split())) for _ in range(N)]

inter_lines = {}
for start, end in lines_lst:
    for i in range(start, end):
        if i in inter_lines:
            inter_lines[i] += 1
        else:
            inter_lines[i] = 1

print(max(inter_lines.values()))
N = int(input())

cur_pos = 0
visited = {}
for _ in range(N):
    size, mv_dir = input().split()
    size = int(size)
    if mv_dir == 'R':
        for i in range(size):
            if not cur_pos + i in visited.keys():
                visited[cur_pos + i] = 1
            else:
                visited[cur_pos + i] += 1
        cur_pos += size
    elif mv_dir == 'L':
        for i in range(1, size + 1):
            if not cur_pos - i in visited.keys():
                visited[cur_pos - i] = 1
            else:
                visited[cur_pos - i] += 1
        cur_pos -= size

cnts = 0
for pos, pos_cnts in visited.items():
    if pos_cnts >= 2:
        cnts += 1

print(cnts)
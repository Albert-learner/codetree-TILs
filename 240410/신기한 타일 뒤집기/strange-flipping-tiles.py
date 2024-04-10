N = int(input())

colored = [0] * 200001
cur_pos = 100000
for _ in range(N):
    size, mv_dir = input().split()
    size = int(size)

    if mv_dir == 'R':
        for i in range(cur_pos, cur_pos + size):
            colored[i] = 1
        cur_pos += size - 1
    else:
        for i in range(cur_pos, cur_pos - size, -1):
            colored[i] = 2
        cur_pos -= size - 1

print(colored.count(2), colored.count(1))
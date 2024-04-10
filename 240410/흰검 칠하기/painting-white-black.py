N = int(input())

colored = [0] * 200001
cur_dir = 100000

white, black = [0] * 200001, [0] * 200001
w, b, g = 0, 0, 0


for _ in range(N):
    size, mv_dir = input().split()
    size = int(size)

    if mv_dir == 'R':
        for i in range(cur_dir, cur_dir + size):
            colored[i] = 2
            black[i] += 1
        cur_dir += size - 1
    else:
        for i in range(cur_dir - size + 1, cur_dir + 1):
            colored[i] = 1
            white[i] += 1
        cur_dir -= size - 1

for i in range(len(colored)):
    if white[i] >= 2 and black[i] >= 2:
        g += 1
    elif colored[i] == 1:
        w += 1
    elif colored[i] == 2:
        b += 1

print(w, b, g)
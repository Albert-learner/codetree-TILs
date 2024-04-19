N = int(input())
people = []
for _ in range(N):
    pos, alpha = input().split()
    pos = int(pos)
    people.append([pos, alpha])

line = [0] * 101
for pos, alpha in people:
    line[pos] = alpha

answer = 0
for i in range(len(line)):
    for j in range(i + 1, len(line)):
        if line[i] == 0 or line[j] == 0:
            continue

        cnt_g, cnt_h = 0, 0
        for k in range(i, j + 1):
            if line[k] == 'G':
                cnt_g += 1
            elif line[k] == 'H':
                cnt_h += 1

        if cnt_g == 0 or cnt_h == 0 or cnt_g == cnt_h:
            length = j - i
            answer = max(answer, length)

print(answer)
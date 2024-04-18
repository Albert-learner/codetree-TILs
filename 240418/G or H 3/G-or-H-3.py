N, K = map(int, input().split())
people = []
for _ in range(N):
    pos, alpha = input().split()
    pos = int(pos)
    people.append([pos, alpha])

scale = 0
K += 1
line = [0] * 20001
for pos, alpha in people:
    if alpha == 'G':
        line[pos] = 1
    else:
        line[pos] = 2
    
    scale = max(scale, pos)

result = 0
for i in range(1, K + 1):
    result += line[i]

cur = result
for i in range(2, scale + 1):
    cur = cur - line[i - 1] + line[i + K - 1]
    result = max(result, cur)

print(result)
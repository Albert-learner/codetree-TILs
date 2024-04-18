N, K = map(int, input().split())
people = []
for _ in range(N):
    pos, alpha = input().split()
    pos = int(pos)
    people.append([pos, alpha])

line = [0] * 10001
for pos, alpha in people:
    if alpha == 'G':
        line[pos] = 1
    else:
        line[pos] = 2

max_sum = 0
for i in range(1, 1000 - K + 1):
    max_sum = max(max_sum, sum(line[i:i + K + 1]))

print(max_sum)
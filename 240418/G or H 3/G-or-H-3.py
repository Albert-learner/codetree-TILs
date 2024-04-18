N, K = map(int, input().split())
people = []
for _ in range(N):
    pos, alpha = input().split()
    pos = int(pos) - 1
    people.append([pos, alpha])

line = [0] * (max(list(zip(*people))[0]) + 1)
for pos, alpha in people:
    if alpha == 'G':
        line[pos] = 1
    else:
        line[pos] = 2

max_sum = 0
for i in range(len(line) - K):
    max_sum = max(max_sum, sum(line[i:i + K + 1]))

print(max_sum)
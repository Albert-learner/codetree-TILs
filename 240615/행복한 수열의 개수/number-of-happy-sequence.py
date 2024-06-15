N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

happy_sequences = 0
for row in board:
    for i in range(N - M + 1):
        if row[i:i + M].count(row[i]) == M:
            happy_sequences += 1
            break

for col in zip(*board):
    for i in range(N - M + 1):
        if col[i:i + M].count(col[i]) == M:
            happy_sequences += 1
            break

print(happy_sequences)
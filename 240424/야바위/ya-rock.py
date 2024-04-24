N = int(input())

max_score = 0
for _ in range(N):
    a, b, c = map(int, input().split())

    tmp = [0, 0, 0]
    tmp[a - 1] = 1
    tmp[b - 1] = 2

    if tmp[c - 1] == 1:
        max_score += 1

print(max_score)
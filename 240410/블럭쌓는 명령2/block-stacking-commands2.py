N, K = map(int, input().split())
blocks = []
for _ in range(K):
    first, second = map(int, input().split())
    blocks.append([first, second])


checked = [0] * (N + 1)
for start, end in blocks:
    for i in range(start, end + 1):
        checked[i] += 1

print(max(checked))
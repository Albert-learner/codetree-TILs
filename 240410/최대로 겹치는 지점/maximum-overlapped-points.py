N = int(input())
checked = [0] * 100

for _ in range(N):
    start, end = map(int, input().split())
    for i in range(start, end + 1):
        checked[i - 1] += 1

print(max(checked))
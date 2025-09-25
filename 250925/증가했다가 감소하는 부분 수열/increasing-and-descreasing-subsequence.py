n = int(input())
sequence = list(map(int, input().split()))

# Please write your code here.
LIS = [1] * n
for i in range(n):
    for j in range(i):
        if sequence[j] < sequence[i]:
            LIS[i] = max(LIS[i], LIS[j] + 1)

LDS = [1] * n
for i in range(n - 1, -1, -1):
    for j in range(i + 1, n):
        if sequence[j] < sequence[i]:
            LDS[i] = max(LDS[i], LDS[j] + 1)

max_seq_len = 0
for i in range(n):
    max_seq_len = max(max_seq_len, LIS[i] + LDS[i] - 1)

print(max_seq_len)
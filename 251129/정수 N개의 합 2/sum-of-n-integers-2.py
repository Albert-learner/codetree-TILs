n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
max_sum = 0

seq_ks = [arr[i:i + k] for i in range(n - k + 1)]
for seq_k in seq_ks:
    seq_sum = sum(seq_k)
    max_sum = max(max_sum, seq_sum)

print(max_sum)
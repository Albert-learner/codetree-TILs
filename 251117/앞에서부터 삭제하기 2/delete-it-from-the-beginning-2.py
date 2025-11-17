n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
suffix_sum = [0] * (n + 1)
for i in range(n - 1, -1, -1):
    suffix_sum[i] = suffix_sum[i + 1] + arr[i]

suffix_min = [0] * n
cur_min = 10 ** 9
for i in range(n - 1, -1, -1):
    if arr[i] < cur_min:
        cur_min = arr[i]
    suffix_min[i] = cur_min

max_avg = 0.0

for k in range(1, n - 1):
    length = n - k         
    if length <= 1:
        continue            
    total = suffix_sum[k]
    mn = suffix_min[k]
    avg = (total - mn) / (length - 1)
    if avg > max_avg:
        max_avg = avg

print(f"{max_avg:.2f}")
    
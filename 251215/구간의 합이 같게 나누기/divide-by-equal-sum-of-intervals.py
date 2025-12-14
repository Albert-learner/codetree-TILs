n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
total = sum(arr)

if total % 4 != 0:
    print(0)
    exit()

t1 = total // 4
t2 = 2 * t1
t3 = 3 * t1

prefix = [0] * n
prefix[0] = arr[0]
for i in range(1, n):
    prefix[i] = prefix[i - 1] + arr[i]

suffix3 = [0] * n
cnt = 0
for i in range(n - 2, -1, -1):
    if prefix[i] == t3:
        cnt += 1
    suffix3[i] = cnt
suffix3[-1] = 0

ans = 0
cnt_t1 = 0

for j in range(1, n - 1):
    if prefix[j - 1] == t1:
        cnt_t1 += 1

    if prefix[j] == t2 and j + 1 < n:
        ans += cnt_t1 * suffix3[j + 1]

print(ans)
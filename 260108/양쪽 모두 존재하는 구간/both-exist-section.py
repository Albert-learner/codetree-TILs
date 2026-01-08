n, m = map(int, input().split())
arr = [0] + list(map(int, input().split()))

# Please write your code here.
import sys

INT_MAX = sys.maxsize

cnt_arr_in = [0] * (m + 1)
cnt_arr_out = [0] * (m + 1)

dist_num_in, dist_num_out = 0, 0

def push(idx):
    global dist_num_in, dist_num_out
    num = arr[idx]

    if cnt_arr_in[num] == 0:
        dist_num_in += 1
    cnt_arr_in[num] += 1

    cnt_arr_out[num] -= 1
    if cnt_arr_out[num] == 0:
        dist_num_out -= 1

def pop(idx):
    global dist_num_in, dist_num_out
    num = arr[idx]

    cnt_arr_in[num] -= 1
    if cnt_arr_in[num] == 0:
        dist_num_in -= 1

    if cnt_arr_out[num] == 0:
        dist_num_out += 1
    cnt_arr_out[num] += 1


for i in range(1, n + 1):
    if cnt_arr_out[arr[i]] == 0:
        dist_num_out += 1

    cnt_arr_out[arr[i]] += 1

ans = INT_MAX

j = 0
for i in range(1, n + 1):
    while j + 1 <= n and dist_num_in < m:
        push(j + 1)
        j += 1

    if dist_num_in < m:
        break

    if dist_num_out == m:
        ans = min(ans, j - i + 1)

    pop(i)

if ans == INT_MAX:
    ans = -1

print(ans)
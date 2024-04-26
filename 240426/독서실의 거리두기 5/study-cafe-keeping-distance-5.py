import sys

N = int(input())
bin_str_lst = list(input())

answer = 0
for i in range(N):
    if bin_str_lst[i] == '1':
        continue

    tmp = sys.maxsize
    fill_poses = [j for j in range(N) if bin_str_lst[j] == '1' or i == j]
    for j in range(len(fill_poses) - 1):
        tmp = min(tmp, fill_poses[j + 1] - fill_poses[j])

    answer = max(answer, tmp)

print(answer)
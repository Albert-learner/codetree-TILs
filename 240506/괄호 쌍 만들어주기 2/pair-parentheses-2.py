a_str = input()

front_idxs, rear_idxs = [], []
for chr_idx, a_chr in enumerate(a_str):
    if a_chr == '(':
        front_idxs.append(chr_idx)
    else:
        rear_idxs.append(chr_idx)

answer = 0
for i in range(len(front_idxs) - 1):
    if abs(front_idxs[i + 1] - front_idxs[i]) == 1:
        for j in range(i + 1, len(rear_idxs) - 1):
            if abs(rear_idxs[j + 1] - rear_idxs[j]) == 1:
                answer += 1

print(answer)
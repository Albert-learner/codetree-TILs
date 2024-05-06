a_str = input()

front_idxs, rear_idxs = [], []
for chr_idx, a_chr in enumerate(a_str):
    if a_chr == '(':
        front_idxs.append(chr_idx)
    else:
        rear_idxs.append(chr_idx)

answer = 0
front_cases, rear_cases = 0, 0
for i in range(len(front_idxs) - 1):
    if abs(front_idxs[i + 1] - front_idxs[i]) == 1:
        front_cases += 1

for i in range(len(rear_idxs) - 1):
    if abs(rear_idxs[i + 1] - rear_idxs[i]) == 1:
        rear_cases += 1

answer = front_cases * rear_cases
print(answer)
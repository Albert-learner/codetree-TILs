N = int(input())
a_scores = [0] * (N + 1)
b_scores = [0] * (N + 1)

idx, cnts = 0, 0
for _ in range(N):
    c, s = input().split()
    ch_score = int(s)
    idx += 1

    if a_scores[idx] == a_scores[idx - 1] and b_scores[idx] == b_scores[idx - 1]:
        a_scores[idx], b_scores[idx] = a_scores[idx - 1], b_scores[idx - 1]

    if c == 'A':
        a_scores[idx] = a_scores[idx - 1] + ch_score
    elif c == 'B':
        b_scores[idx] = b_scores[idx - 1] + ch_score

    

for i in range(N):
    if (a_scores[i] == b_scores[i] and a_scores[i + 1] > b_scores[i + 1]) or \
       (a_scores[i] == b_scores[i] and a_scores[i + 1] < b_scores[i + 1]) or \
       (a_scores[i] > b_scores[i] and a_scores[i + 1] == b_scores[i + 1]) or \
       (a_scores[i] > b_scores[i] and a_scores[i + 1] < b_scores[i + 1]) or \
       (a_scores[i] < b_scores[i] and a_scores[i + 1] == b_scores[i + 1]) or \
       (a_scores[i] < b_scores[i] and a_scores[i + 1] > b_scores[i + 1]):
       cnts += 1

print(cnts)
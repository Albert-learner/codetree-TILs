from itertools import permutations

N, M = map(int, input().split())
a_seq = list(map(int, input().split()))
b_seq = list(map(int, input().split()))

beautiful_seq = list(map(list, permutations(b_seq, len(b_seq))))

answer = 0
for a_idx, a in enumerate(a_seq):
    if a_seq[a_idx:a_idx + len(b_seq)] in beautiful_seq:
        answer += 1

print(answer)
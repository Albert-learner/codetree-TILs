N, M = map(int, input().split())
a_seq = list(map(int, input().split()))
b_seq = list(map(int, input().split()))

def permute_iter(lst):
    stack = [(0, [])]
    result = []

    while stack:
        index, path = stack.pop()
        if index == len(lst):
            result.append(path)
        else:
            for i in range(len(lst)):
                if lst[i] not in path:
                    stack.append((index + 1, path + [lst[i]]))

    return result

answer = 0
beautiful_seq = permute_iter(b_seq)
for a_idx in range(N - M + 1):
    if a_seq[a_idx:a_idx + M] in beautiful_seq:
        answer += 1

print(answer)
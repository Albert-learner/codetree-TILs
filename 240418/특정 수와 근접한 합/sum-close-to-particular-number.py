N, S = map(int, input().split())
n_lst = list(map(int, input().split()))

def exclude_two_elements(lst, i, j):
    result = [x for idx, x in enumerate(lst) if idx != i and idx != j]

    return result

def generate_all_exclusions(lst):
    exclusions = []
    for i in range(N):
        for j in range(i + 1, N):
            exclusion = exclude_two_elements(lst, i, j)
            exclusions.append(sum(exclusion))

    return exclusions

diffs = sorted(generate_all_exclusions(n_lst), key = lambda x: abs(S - x))
print(abs(diffs[0] - S))
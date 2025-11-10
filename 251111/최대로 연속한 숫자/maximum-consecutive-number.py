n, m = map(int, input().split())
nums = list(map(int, input().split()))

# Please write your code here.
n_lst = [i for i in range(n + 1)]

def split_consecutive_sequences(lst):
    if not lst:
        return []

    lst = sorted(lst)
    result = []
    current = [lst[0]]

    for i in range(1, len(lst)):
        if lst[i] == lst[i - 1] + 1:
            current.append(lst[i])
        else:
            result.append(current)
            current = [lst[i]]

    result.append(current)
    return result

for num in nums:
    n_lst.remove(num)
    max_len_seqs = 0
    for divide_seq in split_consecutive_sequences(n_lst):
        if max_len_seqs < len(divide_seq):
            max_len_seqs = len(divide_seq)

    print(max_len_seqs)
T, m = input().split()
m = int(m)
P = input().split()

# Please write your code here.
from array import array

n = len(T)

P = list(set(P))

head = [-1] * (n + 1)
lengths = array('i')
nexts = array('i')

def add_match(end_pos, length):
    lengths.append(length)
    nexts.append(head[end_pos])
    head[end_pos] = len(lengths) - 1

def build_lps(pattern):
    lps = [0] * len(pattern)
    j = 0

    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = lps[j - 1]

        if pattern[i] == pattern[j]:
            j += 1
            lps[i] = j

    return lps

def kmp(pattern):
    lps = build_lps(pattern)
    j = 0
    plen = len(pattern)

    for i in range(n):
        while j > 0 and T[i] != pattern[j]:
            j = lps[j - 1]

        if T[i] == pattern[j]:
            j += 1

            if j == plen:
                end_pos = i + 1
                add_match(end_pos, plen)
                j = lps[j - 1]

for pattern in P:
    kmp(pattern)

dp = [0] * (n + 1)

for i in range(1, n + 1):
    dp[i] = dp[i - 1]

    idx = head[i]
    while idx != -1:
        l = lengths[idx]
        dp[i] = max(dp[i], dp[i - l] + l)
        idx = nexts[idx]

print(dp[n])
T = input()
P = input()

# Please write your code here.
def build_lps(pattern):
    m = len(pattern)
    lps = [0] * m

    j = 0
    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = lps[j - 1]

        if pattern[i] == pattern[j]:
            j += 1
            lps[i] = j

    return lps

def kmp(text, pattern):
    lps = build_lps(pattern)

    positions = []
    j = 0

    for i in range(len(text)):
        while j > 0 and text[i] != pattern[j]:
            j = lps[j - 1]

        if text[i] == pattern[j]:
            j += 1

            if j == len(pattern):
                positions.append(i - len(pattern) + 1)
                j = lps[j - 1]

    return positions

positions = kmp(T, P)

cnt = 0
last_end = -1
plen = len(P)

for start in positions:
    if start > last_end:
        cnt += 1
        last_end = start + plen - 1

print(cnt)
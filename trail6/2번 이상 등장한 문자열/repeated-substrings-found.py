S = input().strip()

# Please write your code here.
n = len(S)

sa = list(range(n))
rank = [ord(c) for c in S]
tmp = [0] * n

k = 1
while k < n:
    sa.sort(key=lambda x: (rank[x], rank[x + k] if x + k < n else -1))

    tmp[sa[0]] = 0

    for i in range(1, n):
        prev = sa[i - 1]
        cur = sa[i]

        prev_key = (rank[prev], rank[prev + k] if prev + k < n else -1)
        cur_key = (rank[cur], rank[cur + k] if cur + k < n else -1)

        if prev_key == cur_key:
            tmp[cur] = tmp[prev]
        else:
            tmp[cur] = tmp[prev] + 1

    rank, tmp = tmp, rank

    if rank[sa[-1]] == n - 1:
        break

    k *= 2

lcp = [0] * n
h = 0

for i in range(n):
    r = rank[i]

    if r == 0:
        continue

    j = sa[r - 1]

    while i + h < n and j + h < n and S[i + h] == S[j + h]:
        h += 1

    lcp[r] = h

    if h > 0:
        h -= 1

print(max(lcp))
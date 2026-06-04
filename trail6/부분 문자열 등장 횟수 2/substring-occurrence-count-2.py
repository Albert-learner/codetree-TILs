T, q = input().split()
q = int(q)
P = [input() for _ in range(q)]

# Please write your code here.
text = '#' + T

for pat in P:
    if pat not in T:
        print(0)
        continue

    pattern = '#' + pat
    n, m = len(T), len(pat)

    f = [0] * (m + 1)

    f[0] = -1
    sub_cnts = 0
    for i in range(1, m + 1):
        j = f[i - 1]
        while j >= 0 and pattern[j + 1] != pattern[i]:
            j = f[j]
        f[i] = j + 1

    j = 0
    for i in range(1, n + 1):
        while j >= 0 and pattern[j + 1] != text[i]:
            j = f[j]
        j += 1

        if j == m:
            sub_cnts += 1
            j = f[j]

    print(sub_cnts)
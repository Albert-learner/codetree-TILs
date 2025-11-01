n, m = map(int, input().split())

A = [input() for _ in range(n)]
B = [input() for _ in range(n)]

# Please write your code here.
chr_dict = {'A': 0, 'C': 1, 'G': 2, 'T': 3}

def code3(s, i, j, k):
    return chr_dict[s[i]] * 16 + chr_dict[s[j]] * 4 + chr_dict[s[k]]

ans = 0
for i in range(m - 2):
    for j in range(i + 1, m - 1):
        for k in range(j + 1, m):
            seenA = [False] * 64

            for s in A:
                seenA[code3(s, i, j, k)] = True

            ok = True
            for s in B:
                if seenA[code3(s, i, j, k)]:
                    ok = False
                    break

            if ok:
                ans += 1

print(ans)

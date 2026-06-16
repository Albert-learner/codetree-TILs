T, m = input().split()
m = int(m)
P = input().split()

# Please write your code here.
MOD = 10 ** 9 + 7

n = len(T)
trie = [{}]
terminal = [False]

for pattern in set(P):
    cur = 0

    for ch in pattern:
        if ch not in trie[cur]:
            trie[cur][ch] = len(trie)
            trie.append({})
            terminal.append(False)

        cur = trie[cur][ch]

    terminal[cur] = True

dp = [0] * (n + 1)
dp[0] = 1

for i in range(n):
    if dp[i] == 0:
        continue

    cur = 0
    for j in range(i, n):
        ch = T[j]

        if ch not in trie[cur]:
            break

        cur = trie[cur][ch]

        if terminal[cur]:
            dp[j + 1] = (dp[j + 1] + dp[i]) % MOD

print(dp[n])
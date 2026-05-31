l, S = input().split()
l = int(l)

# Please write your code here.
from collections import defaultdict

n = len(S)

MOD1 = 10 ** 9 + 7
MOD2 = 10 ** 9 + 9
BASE = 911382323

pow1 = [1] * (n + 1)
pow2 = [1] * (n + 1)

for i in range(n):
    pow1[i + 1] = (pow1[i] * BASE) % MOD1
    pow2[i + 1] = (pow2[i] * BASE) % MOD2

hash1 = [0] * (n + 1)
hash2 = [0] * (n + 1)

for i, ch in enumerate(S):
    num = ord(ch) - ord('a') + 1
    hash1[i + 1] = (hash1[i] * BASE + num) % MOD1
    hash2[i + 1] = (hash2[i] * BASE + num) % MOD2

cnt = defaultdict(int)
answer = 0

for i in range(n - l + 1):
    h1 = (hash1[i + l] - hash1[i] * pow1[l]) % MOD1
    h2 = (hash2[i + l] - hash2[i] * pow2[l]) % MOD2

    key = (h1, h2)
    cnt[key] += 1

    if cnt[key] > answer:
        answer = cnt[key]

print(answer)
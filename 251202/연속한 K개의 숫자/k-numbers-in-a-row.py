N, K, B = map(int, input().split())
missing = [int(input()) for _ in range(B)]

# Please write your code here.
broken = [0] * (N + 1)
for x in missing:
    broken[x] = 1

cur = sum(broken[1:K + 1])
answer = cur

for i in range(K + 1, N + 1):
    cur += broken[i]
    cur -= broken[i - K]
    if cur < answer:
        answer = cur

print(answer)
n = int(input())
m = int(input())
k = [int(input()) for _ in range(m)]

# Please write your code here.
parent = list(range(n + 1))

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]

    return x

answer = 0
for limit in k:
    pos = find(limit)

    if pos == 0:
        break

    answer += 1
    parent[pos] = find(pos - 1)

print(answer)
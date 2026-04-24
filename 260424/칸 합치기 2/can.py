n, m = map(int, input().split())
queries = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
import sys

parent = list(range(n + 1))

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    
    return parent[x]

count = n
answer = []

for a, b in queries:
    x = find(a)

    while x < b:
        count -= 1
        parent[x] = find(x + 1)
        x = find(x)
    answer.append(str(count))

print("\n".join(answer))


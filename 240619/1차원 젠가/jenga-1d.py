N = int(input())
blocks = [int(input()) for _ in range(N)]
s1, e1 = map(int, input().split())
s2, e2 = map(int, input().split())

blocks = blocks[:s1 - 1] + blocks[e1:]
blocks = blocks[:s2 - 1] + blocks[e2:]
blocks.insert(0, len(blocks))

for n in blocks:
    print(n)
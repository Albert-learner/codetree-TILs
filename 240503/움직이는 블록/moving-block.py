N = int(input())
blocks = [int(input()) for _ in range(N)]

sum_blocks = sum(blocks)
average = sum_blocks // N

cnts = 0
while blocks.count(average) < N:
    blocks.sort()

    diff = average - blocks[0]
    diff_max = abs(average - blocks[-1])
    blocks[0] += diff
    blocks[-1] -= diff_max

    cnts += diff

print(cnts)
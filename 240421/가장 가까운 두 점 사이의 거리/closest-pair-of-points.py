N = int(input())
coords = [tuple(map(int, input().split())) for _ in range(N)]

dsts = []
for f_idx, (fx, fy) in enumerate(coords):
    for rx, ry in coords[f_idx + 1:]:
        dst = (fx - rx) ** 2 + (fy - ry) ** 2
        dsts.append(dst)

print(min(dsts))
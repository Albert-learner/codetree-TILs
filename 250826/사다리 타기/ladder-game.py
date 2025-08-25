n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
edges.sort(key=lambda x: (x[1], x[0]))

def perm_from_edges(selected):
    p = list(range(1, n + 1))
    for a, _ in selected:
        i = a - 1
        p[i], p[i + 1] = p[i + 1], p[i]

    return p

full_perm = perm_from_edges(edges)

min_h_lines = m
for mask in range(1 << m):
    selected = [edges[i] for i in range(m) if (mask >> i) & 1]
    if perm_from_edges(selected) == full_perm:
        cnts = mask.bit_count()
        if cnts < min_h_lines:
            min_h_lines = cnts

print(min_h_lines)
N, M = map(int, input().split())
w, v = zip(*[tuple(map(int, input().split())) for _ in range(N)])
w, v = list(w), list(v)

# Please write your code here.
items = [(v[i] / w[i], w[i], v[i]) for i in range(N)]
items.sort(reverse = True)

remains = M
total = 0.0

for ratio, wi, vi in items:
    if remains == 0:
        break

    if wi <= remains:
        total += vi
        remains -= wi
    else:
        total += vi * (remains / wi)
        remains = 0

print(f"{total:.3f}")
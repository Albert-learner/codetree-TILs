n, m = map(int, input().split())
segments = [tuple(map(int, input().split())) for _ in range(m)]
segments.sort()

min_a = segments[0][0]
max_b = max(b for _, b in segments)

def can_place(d: int) -> bool:
    if d == 0:
        return True

    cnt = 0
    last = None

    for a, b in segments:
        if last is None:
            pos = a
        else:
            need = last + d
            if need > b:
                continue
            pos = max(a, need)

        if pos > b:
            continue

        add = 1 + (b - pos) // d
        cnt += add
        last = pos + (add - 1) * d

        if cnt >= n:
            return True

    return cnt >= n

lo, hi = 0, max_b - min_a
while lo < hi:
    mid = (lo + hi + 1) // 2
    if can_place(mid):
        lo = mid
    else:
        hi = mid - 1

print(lo)

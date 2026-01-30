N, K, L = map(int, input().split())
c = list(map(int, input().split()))

# Please write your code here.
class Fenwick:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, i, delta):
        i += 1
        while i <= self.n:
            self.bit[i] += delta
            i += i & -i

    def sum_prefix(self, i):
        if i < 0:
            return 0

        i += 1
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i

        return s

    def sum_range(self, l, r):
        if l > r:
            return 0

        return self.sum_prefix(r) - self.sum_prefix(l - 1)

total_slots = K * L
maxV = max(c) if c else 0

bit_cnt = Fenwick(maxV + 1)
bit_sum = Fenwick(maxV + 1)

for v in c:
    bit_cnt.add(v, 1)
    bit_sum.add(v, v)

def can_make(h: int) -> bool:
    if h == 0:
        return True

    if total_slots == 0:
        already = bit_cnt.sum_range(h, maxV) if h <= maxV else 0
        return already >= h

    already = bit_cnt.sum_range(h, maxV) if h <= maxV else 0
    need = h - already
    if need <= 0:
        return True

    l = max(0, h - K)
    u = min(h - 1, maxV)
    if l > u:
        return False

    avail = bit_cnt.sum_range(l, u)
    if avail < need:
        return False

    lo, hi = l, u
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if bit_cnt.sum_range(mid, u) >= need:
            lo = mid
        else:
            hi = mid - 1

    t = lo

    cnt_above = bit_cnt.sum_range(t + 1, u)
    sum_above = bit_sum.sum_range(t + 1, u)
    remain = need - cnt_above
    best_sum_vals = sum_above + remain * t

    required = need * h - best_sum_vals

    return required <= total_slots

lo, hi = 0, N
ans = 0
while lo <= hi:
    mid = (lo + hi) // 2
    if can_make(mid):
        ans = mid
        lo = mid + 1
    else:
        hi = mid - 1

print(ans)
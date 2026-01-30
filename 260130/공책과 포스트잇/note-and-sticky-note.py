import sys
input = sys.stdin.readline

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
        # sum [0..i]
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

N, K, L = map(int, input().split())
c = list(map(int, input().split()))

total_slots = K * L
maxV = max(c) if c else 0

# Fenwick for counts and sums over value v (0..maxV)
bit_cnt = Fenwick(maxV + 1)
bit_sum = Fenwick(maxV + 1)

for v in c:
    bit_cnt.add(v, 1)
    bit_sum.add(v, v)

def can_make(h: int) -> bool:
    if h == 0:
        return True
    if total_slots == 0:
        # 추가 불가면 원래 h-index만 가능한지 체크하면 됨
        already = bit_cnt.sum_range(h, maxV) if h <= maxV else 0
        return already >= h

    # 이미 ci >= h 인 개수
    already = bit_cnt.sum_range(h, maxV) if h <= maxV else 0
    need = h - already
    if need <= 0:
        return True

    # 업그레이드 가능한 후보: ci in [h-K, h-1]
    l = max(0, h - K)
    u = min(h - 1, maxV)
    if l > u:
        return False

    avail = bit_cnt.sum_range(l, u)
    if avail < need:
        return False

    # [l..u]에서 가장 큰 need개 값들의 합을 구한다.
    # threshold t를 찾아서, [t..u]에 need개 이상 존재하도록 하는 최대 t를 찾음.
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
    best_sum_vals = sum_above + remain * t  # need개를 최대합으로 고른 값들의 합

    # 필요한 총 증가량 = need*h - best_sum_vals
    required = need * h - best_sum_vals
    return required <= total_slots

# h는 최대 N까지 가능
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

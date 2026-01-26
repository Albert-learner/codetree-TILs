n = int(input())
x = list(map(int, input().split()))
v = list(map(int, input().split()))

# Please write your code here.
def can_meet(t: float) -> bool:
    left = -1e30
    right = 1e30

    for xi, vi in zip(x, v):
        reach = t * vi
        l = xi - reach
        r = xi + reach
        if l > left:
            left = l
        if r < right:
            right = r
        
        if left > right:
            return False

    return True

lo, hi = 0.0, 1e9
for _ in range(70):
    mid = (lo + hi) / 2
    if can_meet(mid):
        hi = mid
    else:
        lo = mid

print(f"{hi:.4f}")
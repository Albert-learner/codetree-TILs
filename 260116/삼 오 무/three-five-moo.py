n = int(input())

# Please write your code here.
def count_numbers_upto(x: int) -> int:
    moo = x // 3 + x // 5 - x // 15

    return x - moo

lo, hi = 1, 2
while count_numbers_upto(hi) < n:
    hi *= 2

while lo < hi:
    mid = (lo + hi) // 2
    if count_numbers_upto(mid) >= n:
        hi = mid
    else:
        lo = mid + 1

print(lo)
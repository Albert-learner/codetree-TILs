n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
lines_sorted = sorted(((x1, x2, i) for i, (x1, x2) in enumerate(lines)),
                      key = lambda x: x[0])

x2_list = [x2 for _, x2, _ in lines_sorted]
sorted_x2 = sorted(set(x2_list))
comp = {v: i + 1 for i, v in enumerate(sorted_x2)}

class BIT:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)

    def update(self, i, delta):
        while i <= self.n:
            self.tree[i] += delta
            i += i & -i

    def query(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

    def range_sum(self, l, r):
        if l > r:
            return 0
        return self.query(r) - self.query(l - 1)


m = len(sorted_x2)

pos_x2 = [comp[x2] for _, x2, _ in lines_sorted]

left_greater = [0] * n
bit_left = BIT(m)
total = 0
for k in range(n):
    idx = pos_x2[k]
    left_greater[k] = total - bit_left.query(idx)
    bit_left.update(idx, 1)
    total += 1

right_smaller = [0] * n
bit_right = BIT(m)
for k in range(n - 1, -1, -1):
    idx = pos_x2[k]
    right_smaller[k] = bit_right.query(idx - 1)
    bit_right.update(idx, 1)

ans = 0
for k in range(n):
    if left_greater[k] == 0 and right_smaller[k] == 0:
        ans += 1

print(ans)
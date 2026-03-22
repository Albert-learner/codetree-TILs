n = int(input())
pre_order = list(map(int, input().split()))
in_order = list(map(int, input().split()))

# Please write your code here.
import sys
sys.setrecursionlimit(200000)

pos = {value:idx for idx, value in enumerate(in_order)}

result = []

def build(pre_l, pre_r, in_l, in_r):
    if pre_l > pre_r:
        return

    root = pre_order[pre_l]
    root_idx = pos[root]

    left_size = root_idx - in_l

    build(pre_l + 1, pre_l + left_size, in_l, root_idx - 1)
    build(pre_l + left_size + 1, pre_r, root_idx + 1, in_r)

    result.append(root)

build(0, n - 1, 0, n - 1)
print(*result)
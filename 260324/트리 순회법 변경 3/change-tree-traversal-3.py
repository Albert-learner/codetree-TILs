n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

# Please write your code here.
import sys
sys.setrecursionlimit(200000)

pos = {value:idx for idx, value in enumerate(inorder)}
result = []

def build(in_l, in_r, post_l, post_r):
    if in_l > in_r:
        return

    root = postorder[post_r]
    result.append(root)

    root_idx = pos[root]
    left_size = root_idx - in_l

    build(in_l, root_idx - 1, post_l, post_l + left_size - 1)
    build(root_idx + 1, in_r, post_l + left_size, post_r - 1)

build(0, n - 1, 0, n - 1)
print(*result)
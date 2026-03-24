n = int(input())
pre_order = [int(input()) for _ in range(n)]

# Please write your code here.
import sys
sys.setrecursionlimit(200000)


def build(start, end):
    if start > end:
        return

    root = pre_order[start]

    idx = start + 1
    while idx <= end and pre_order[idx] < root:
        idx += 1

    build(start + 1, idx - 1)
    build(idx, end)

    print(root)

build(0, n - 1)
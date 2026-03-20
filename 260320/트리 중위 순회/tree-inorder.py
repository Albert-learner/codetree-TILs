K = int(input())
inorder_traversal = list(map(int, input().split()))

# Please write your code here.
def build_tree(inorder, level, tree):
    if not inorder:
        return

    mid = len(inorder) // 2
    root = inorder[mid]

    tree[level].append(root)

    build_tree(inorder[:mid], level + 1, tree)
    build_tree(inorder[mid + 1:], level + 1, tree)

tree = [[] for _ in range(K)]
build_tree(inorder_traversal, 0, tree)

for level in tree:
    print(*level)

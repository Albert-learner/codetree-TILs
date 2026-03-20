n = int(input())

left = [0] * 26
right = [0] * 26

for _ in range(n):
    x, l, r = input().split()
    left[ord(x) - ord("A")] = l
    right[ord(x) - ord("A")] = r

# Please write your code here.
preorder_lst = []
inorder_lst = []
postorder_lst = []

def preorder(node):
    if node == ".":
        return

    idx = ord(node) - ord("A")
    preorder_lst.append(node)
    preorder(left[idx])
    preorder(right[idx])

def inorder(node):
    if node == ".":
        return

    idx = ord(node) - ord("A")
    inorder(left[idx])
    inorder_lst.append(node)
    inorder(right[idx])

def postorder(node):
    if node == ".":
        return

    idx = ord(node) - ord("A")
    postorder(left[idx])
    postorder(right[idx])
    postorder_lst.append(node)

preorder("A")
inorder("A")
postorder("A")

print("".join(preorder_lst))
print("".join(inorder_lst))
print("".join(postorder_lst))

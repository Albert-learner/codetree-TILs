A = input()
B = input()

# Please write your code here.
stack = []
blen = len(B)

for ch in A:
    stack.append(ch)

    if len(stack) >= blen:
        if "".join(stack[-blen:]) == B:
            for _ in range(blen):
                stack.pop()

print("".join(stack))
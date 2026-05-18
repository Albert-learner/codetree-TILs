n = int(input())
signs = input().split()

# Please write your code here.
def make_min():
    result = []
    stack = []

    for i in range(n):
        stack.append(i + 1)

        if i == n - 1 or signs[i] == '<':
            while stack:
                result.append(stack.pop())

    return result

def make_max():
    result = []
    stack = []

    for i in range(n):
        stack.append(n - i)

        if i == n - 1 or signs[i] == '>':
            while stack:
                result.append(stack.pop())

    return result

min_seq = make_min()
max_seq = make_max()

print("".join(f"{x:03d}" for x in min_seq))
print("".join(f"{x:03d}" for x in max_seq))
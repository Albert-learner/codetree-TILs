N = int(input())
a = input()
b = input()

# Please write your code here.
ans = 0
in_block = False

for i in range(N):
    diff = (a[i] != b[i])
    if diff and not in_block:
        ans += 1
        in_block = True
    elif not diff:
        in_block = False

print(ans)
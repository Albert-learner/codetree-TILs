n = int(input())
numbers = [int(input()) for _ in range(n)]

# Please write your code here.
first = [-1] * 7
first[0] = 0
prefix, ans = 0, 0

for i in range(1, n + 1):
    prefix = (prefix + numbers[i - 1]) % 7

    if first[prefix] == -1:
        first[prefix] = i
    else:
        ans = max(ans, i - first[prefix])

print(ans)
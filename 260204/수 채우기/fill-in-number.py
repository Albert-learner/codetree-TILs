n = int(input())

# Please write your code here.
ans = float("inf")

for five in range(n // 5, -1, -1):
    rest = n - 5 * five
    if rest % 2 == 0:
        ans = min(ans, five + rest // 2)
        break

print(ans if ans != float("inf") else -1)
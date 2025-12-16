n, q = map(int, input().split())
arr = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(q)]

# Please write your code here.
prefix_max = [0] * n
prefix_max[0] = arr[0]
for i in range(1, n):
    prefix_max[i] = max(prefix_max[i - 1], arr[i])

suffix_max = [0] * n
suffix_max[n - 1] = arr[n - 1]
for i in range(n - 2, -1, -1):
    suffix_max[i] = max(suffix_max[i + 1], arr[i])

out = []
for a, b in queries:
    l = a - 1
    r = b - 1

    left_max = prefix_max[l - 1] if l - 1 >= 0 else -1
    right_max = suffix_max[r + 1] if r + 1 < n else -1

    out.append(str(max(left_max, right_max)))

print("\n".join(out))
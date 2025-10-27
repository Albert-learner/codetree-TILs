n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
first_pos = {}
for i, x in enumerate(arr, 1):
    if x not in first_pos:
        first_pos[x] = i

out_lines = []
for x in sorted(first_pos.keys()):
    out_lines.append(f"{x} {first_pos[x]}")
print("\n".join(out_lines))

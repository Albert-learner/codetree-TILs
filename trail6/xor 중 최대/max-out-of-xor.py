n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
answer = 0
mask = 0

for bit in range(30, -1, -1):
    mask |= (1 << bit)

    prefixes = set()
    for num in arr:
        prefixes.add(num & mask)

    candidate = answer | (1 << bit)

    possible = False
    for p in prefixes:
        if (candidate ^ p) in prefixes:
            possible = True
            break

    if possible:
        answer = candidate

print(answer)
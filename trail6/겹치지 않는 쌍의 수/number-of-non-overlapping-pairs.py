n = int(input())
m = []
groups = []

for _ in range(n):
    nums = list(map(int, input().split()))
    m.append(nums[0])
    groups.append(nums[1:])

# Please write your code here.
masks = []

for group in groups:
    mask = 0
    for person in group:
        mask |= 1 << (person - 1)
    masks.append(mask)

answer = 0

for i in range(n):
    for j in range(i + 1, n):
        if masks[i] & masks[j] == 0:
            answer += 1

print(answer)
n = int(input())
words = input().split()

# Please write your code here.
child = []
count = []
depth = []

child.append({})
count.append(0)
depth.append(0)

answer = 0

for word in words:
    cur = 0

    for ch in word:
        if ch not in child[cur]:
            child[cur][ch] = len(child)
            child.append({})
            count.append(0)
            depth.append(depth[cur] + 1)

        cur = child[cur][ch]
        count[cur] += 1

        value = depth[cur] * count[cur]
        if value > answer:
            answer = value

print(answer)
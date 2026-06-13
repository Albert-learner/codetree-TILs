n, m = map(int, input().split())
words = input().split()
S = input()

# Please write your code here.
child, count = [], []

child.append({})
count.append(0)

for word in words:
    cur = 0
    count[cur] += 1

    for ch in word:
        if ch not in child[cur]:
            child[cur][ch] = len(child)
            child.append({})
            count.append(0)

        cur = child[cur][ch]
        count[cur] += 1

answer = []

cur = 0
valid = True

for ch in S:
    if valid and ch in child[cur]:
        cur = child[cur][ch]
        answer.append(str(count[cur]))
    else:
        valid = False
        answer.append("0")

print(" ".join(answer))
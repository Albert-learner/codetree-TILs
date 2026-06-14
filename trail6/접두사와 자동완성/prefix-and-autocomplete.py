n = int(input())
words = input().split()

# Please write your code here.
children = []
terminal = []

children.append({})
terminal.append(False)

def insert(word):
    cur = 0
    for ch in word:
        if ch not in children[cur]:
            children[cur][ch] = len(children)
            children.append({})
            terminal.append(False)
        cur = children[cur][ch]
    terminal[cur] = True

for word in words:
    insert(word)

def count_typing(word):
    cur, idx, typed = 0, 0, 0

    while idx < len(word):
        ch = word[idx]
        typed += 1
        cur = children[cur][ch]
        idx += 1

        while idx < len(word) and not terminal[cur] and len(children[cur]) == 1:
            next_ch = next(iter(children[cur]))
            cur = children[cur][next_ch]
            idx += 1

    return typed

answer = []
for word in words:
    answer.append(count_typing(word))

print(*answer)
word, k = input().split()
k = int(k)

# Please write your code here.
cnts = [0] * 26
distinct = 0

ans, l = 0, 0
for r, ch in enumerate(word):
    idx = ord(ch) - ord('a')
    if cnts[idx] == 0:
        distinct += 1
    cnts[idx] += 1

    while distinct > k:
        left_idx = ord(word[l]) - ord('a')
        cnts[left_idx] -= 1
        if cnts[left_idx] == 0:
            distinct -= 1
        l += 1

    ans = max(ans, r - l + 1)

print(ans)
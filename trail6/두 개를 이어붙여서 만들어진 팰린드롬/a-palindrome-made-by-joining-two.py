n = int(input())
words = input().split()

# Please write your code here.
word_set = set(words)

def is_pal(s, l, r):
    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True

answer = 0

for w in words:
    L = len(w)

    for cut in range(L + 1):
        if is_pal(w, 0, cut - 1):
            cand = w[cut:][::-1]
            if cand in word_set and cand != w:
                answer = max(answer, len(cand) + L)

        if is_pal(w, cut, L - 1):
            cand = w[:cut][::-1]
            if cand in word_set and cand != w:
                answer = max(answer, L + len(cand))

print(answer)
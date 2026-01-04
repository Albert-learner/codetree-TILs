word = input()

# Please write your code here.
word_lst = list(word)
word_len = len(word_lst)
ans = 0

for i in range(word_len):
    w_set = set()
    for j in range(i, word_len):
        if word_lst[j] in w_set:
            ans = max(ans, len(w_set))
            break
        else:
            w_set.add(word_lst[j])

    if len(w_set) != 0:
        ans = max(ans, len(w_set))

print(ans)
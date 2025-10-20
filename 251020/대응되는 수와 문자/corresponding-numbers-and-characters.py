n, m = map(int, input().split())

# Note: Using 1-based indexing for words as per C++ code
words = [""] + [input() for _ in range(n)]
queries = [input() for _ in range(m)]

# Please write your code here.
words_dict = {str(word_idx): word for word_idx, word in enumerate(words[1:], 1)}
words_rev_dict = {word: word_idx for word_idx, word in enumerate(words[1:], 1)}

for query in queries:
    if query in words_dict.keys():
        print(words_dict[query])

    if query in words_rev_dict.keys():
        print(words_rev_dict[query])
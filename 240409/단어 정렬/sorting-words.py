N = int(input())
words = [input() for _ in range(N)]

words.sort()

for word in words:
    print(word)
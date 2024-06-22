N = int(input())
words = [input() for _ in range(N)]
find_chr = input()

cnts, avg_len = 0, 0
answer = []
for word in words:
    if word.startswith(find_chr):
        answer.append(word)
        cnts += 1

avg_len = sum([len(word) for word in answer]) / len(answer)

print(cnts, "{:.2f}".format(avg_len))
words = [input() for _ in range(10)]
find_chr = input()

answer = []
for word in words:
    if word.endswith(find_chr):
        answer.append(word)

if len(answer) == 0:
    print("None")
else:
    for word in answer:
        print(word)
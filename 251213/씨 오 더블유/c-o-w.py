n = int(input())
word = input()

# Please write your code here.
suffix_w = [0] * (n + 1)
for i in range(n - 1, -1, -1):
    suffix_w[i] = suffix_w[i + 1] + (1 if word[i] == 'W' else 0)

cnt_c = 0
answer = 0

for i in range(n):
    if word[i] == 'C':
        cnt_c += 1
    elif word[i] == 'O':
        answer += cnt_c * suffix_w[i + 1]

print(answer)
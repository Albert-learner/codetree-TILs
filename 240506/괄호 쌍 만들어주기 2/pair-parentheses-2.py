a_str = input()

answer = 0
for i in range(len(a_str) - 1):
    for j in range(i + 1, len(a_str) - 1):
        if a_str[i] == '(' and a_str[i + 1] == '(' and a_str[j] == ')' and a_str[j + 1] == ')':
            answer += 1

print(answer)
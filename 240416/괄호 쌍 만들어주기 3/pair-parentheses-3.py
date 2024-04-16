a_str = input()

answer = 0
for i in range(len(a_str)):
    for j in range(i + 1, len(a_str)):
        if a_str[i] == '(' and a_str[j] == ')':
            answer += 1

print(answer)
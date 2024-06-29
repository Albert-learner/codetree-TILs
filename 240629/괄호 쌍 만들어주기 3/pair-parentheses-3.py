a_str = input()

cases = 0
for i in range(len(a_str)):
    for j in range(i + 1, len(a_str)):
        if a_str[i] == '(' and a_str[j] == ')':
            cases += 1

print(cases)
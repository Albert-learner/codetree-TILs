a_str = input()
n = len(a_str)

cnts, result = 0, 0
for i in range(n - 1, 0, -1):
    if a_str[i] == ')' and a_str[i - 1] == ')':
        cnts += 1
    elif a_str[i] == '(' and a_str[i - 1] == '(':
        result += cnts

print(result)
a_str = input()
b_str = input()

a_len, b_len = len(a_str), len(b_str)

answer = 0
for i in range(a_len - b_len + 1):
    if a_str[i:i + b_len] == b_str:
        answer += 1

print(answer)
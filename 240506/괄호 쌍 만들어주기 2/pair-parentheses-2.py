a_str = input()
n = len(a_str)

cnts, result = 0, 0
for i in range(n - 1, 0, -1):
    if a_str[i] == ')' and a_str[i - 1] == ')':
        cnts += 1
    elif a_str[i] == '(' and a_str[i - 1] == '(':
        result += cnts

print(result)

# # 모범답안
# # 변수 선언 및 입력
# string = input()
# n = len(string)

# # 모든 쌍을 다 잡아봅니다.
# cnt = 0
# for i in range(n - 1):
#     for j in range(i + 1, n - 1):
#         if string[i] == '(' and string[i + 1] == '(' and string[j] == ')' and string[j + 1] == ')':
#             cnt += 1
            
# print(cnt)
brackets = input()
answer = "Yes"

stack = []
for bracket in brackets:
    if bracket == '(':
        stack.append(bracket)
    else:
        if len(stack) == 0:
            answer = "No"
            break
        else:
            stack.pop()

answer = "Yes" if len(stack) == 0 else "No"
print(answer)
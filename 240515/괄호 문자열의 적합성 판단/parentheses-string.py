brackets = input()

stack = []
for bracket in brackets:
    if bracket == '(':
        stack.append(bracket)
    else:
        if len(stack) == 0:
            print("No")            
            break
        stack.pop()

if len(stack) == 0:
    print("Yes")
else:
    print("No")
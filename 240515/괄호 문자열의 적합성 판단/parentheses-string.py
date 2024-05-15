brackets = input()

def confirm_stack(brkts):
    answer = True

    stack = []
    for brkt in brkts:
        if brkt == '(':
            stack.append(brkt)
        else:
            if len(stack) == 0:
                answer = False
                return answer
            else:
                stack.pop()

    answer = len(stack) == 0
    return answer

if confirm_stack(brackets):
    print("Yes")
else:
    print("No")
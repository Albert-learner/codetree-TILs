R, C = map(int, input().split())
rectangle = [list(input().split()) for _ in range(R)]

cases = 0
stack = [(0, 0, 0)]
while stack:
    cnts, r, c = stack.pop()

    if r == R - 1 and c == C - 1 and cnts == 3:
        cases += 1
    else:
        for dr in range(r + 1, R):
            for dc in range(c + 1, C):
                if rectangle[r][c] != rectangle[dr][dc]:
                    stack.append((cnts + 1, dr, dc))

print(cases)
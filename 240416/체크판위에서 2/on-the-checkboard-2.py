R, C = map(int, input().split())
board = [list(input().split()) for _ in range(R)]

answer = 0
stack = [(0, 0, 0, board[0][0])]
while stack:
    cnt, r, c, val = stack.pop()
    if r == R - 1 and c == C - 1 and cnt == 3:
        answer += 1
    else:
        for mr in range(r + 1, R):
            for mc in range(c + 1, C):
                if board[r][c] != board[mr][mc]:
                    stack.append((cnt + 1, mr, mc, board[mr][mc]))

print(answer)
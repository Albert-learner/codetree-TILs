board = [list(map(int, input().split())) for _ in range(4)]
mdir = input()

def move(board, m_dir):
    if m_dir == 'L':
        for i in range(4):
            new_row = [x for x in board[i] if x != 0]  # Remove all zeros
            new_row += [0] * (4 - len(new_row))  # Pad with zeros on the right

            for j in range(3):
                if new_row[j] == new_row[j + 1] and new_row[j] != 0:
                    new_row[j] *= 2
                    new_row[j + 1] = 0

            new_row = [x for x in new_row if x != 0]
            new_row += [0] * (4 - len(new_row))
            board[i] = new_row
    elif m_dir == 'R':
        for i in range(4):
            new_row = [x for x in board[i] if x != 0]  # Remove all zeros
            new_row = [0] * (4 - len(new_row)) + new_row  # Pad with zeros on the left

            for j in range(3, 0, -1):
                if new_row[j] == new_row[j - 1] and new_row[j] != 0:
                    new_row[j] *= 2
                    new_row[j - 1] = 0

            new_row = [x for x in new_row if x != 0]
            new_row = [0] * (4 - len(new_row)) + new_row
            board[i] = new_row
    elif m_dir == 'D':
        for j in range(4):
            new_col = [board[i][j] for i in range(4) if board[i][j] != 0]  # Remove all zeros
            new_col = [0] * (4 - len(new_col)) + new_col  # Pad with zeros at the top

            for i in range(3, 0, -1):
                if new_col[i] == new_col[i - 1] and new_col[i] != 0:
                    new_col[i] *= 2
                    new_col[i - 1] = 0

            new_col = [x for x in new_col if x != 0]
            new_col = [0] * (4 - len(new_col)) + new_col
            for i in range(4):
                board[i][j] = new_col[i]
    elif m_dir == 'U':
        for j in range(4):
            new_col = [board[i][j] for i in range(4) if board[i][j] != 0]  # Remove all zeros
            new_col += [0] * (4 - len(new_col))  # Pad with zeros at the bottom

            for i in range(3):
                if new_col[i] == new_col[i + 1] and new_col[i] != 0:
                    new_col[i] *= 2
                    new_col[i + 1] = 0

            new_col = [x for x in new_col if x != 0]
            new_col += [0] * (4 - len(new_col))
            for i in range(4):
                board[i][j] = new_col[i]
    else:
        raise ValueError

    return board

new_board = move(board, mdir)
for row in new_board:
    print(*row)
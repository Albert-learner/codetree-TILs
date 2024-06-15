N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

def has_consecutive_numbers(lst):
    for i in range(len(lst) - 1):
        if lst[i] == lst[i + 1]:
            return True
    
    return False

def check_consecutive(matrix):
    row, col = len(matrix), len(matrix[0])
    happy_sequences = 0

    for i in range(row):
        if has_consecutive_numbers(matrix[i]):
            happy_sequences += 1

    for j in range(col):
        column = [matrix[i][j] for i in range(row)]
        if has_consecutive_numbers(column):
            happy_sequences += 1

    return happy_sequences

print(check_consecutive(board))
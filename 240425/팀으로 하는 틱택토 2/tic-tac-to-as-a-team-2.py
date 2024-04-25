board = [list(map(int, input())) for _ in range(3)]

teams = set()
for i in range(3):
    chk = set()
    for j in range(3):
        chk.add(board[i][j])
    
    if len(chk) == 2:
        teams.add(tuple(sorted(chk)))

for j in range(3):
    chk = set()
    for i in range(3):
        chk.add(board[i][j])
    
    if len(chk) == 2:
        teams.add(tuple(sorted(chk)))

chk = set()
for i in range(3):
    chk.add(board[i][i])

if len(chk) == 2:
    teams.add(tuple(sorted(chk)))

chk = set()
for i in range(3):
    chk.add(board[i][2 - i])
if len(chk) == 2:
    teams.add(tuple(sorted(chk)))

print(len(teams))
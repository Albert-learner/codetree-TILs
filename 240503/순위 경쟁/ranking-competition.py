N = int(input())
changes = []
for _ in range(N):
    c, s = input().split()
    ch_score = int(s)
    changes.append([c, ch_score])

a_score, b_score, c_score = 0, 0, 0
change_cnts = 0
prev_winner, winner = 'ABC', 'ABC'
for ch_idx, (player, ch_score) in enumerate(changes):
    if player == 'A':
        a_score += ch_score
    elif player == 'B':
        b_score += ch_score
    elif player == 'C':
        c_score += ch_score

    if ch_idx != 0:
        if a_score > b_score and a_score > c_score:
            winner = 'A'
        elif a_score < b_score and c_score < b_score:
            winner = 'B'
        elif a_score < c_score and b_score < c_score:
            winner = 'C'
        elif a_score < b_score or a_score < c_score:
            winner = 'BC'
        elif b_score < c_score or b_score < a_score:
            winner = 'CA'
        elif c_score < a_score or c_score < b_score:
            winner = 'AB'
        else:
            winner = 'ABC'
    else:
        if a_score < b_score and c_score < b_score:
            winner = 'B'
        elif a_score > b_score and a_score > c_score:
            winner = 'A'
        elif a_score < c_score and b_score < c_score:
            winner = 'C'
        elif a_score < b_score or a_score < c_score:
            winner = 'BC'
        elif b_score < c_score or b_score < a_score:
            winner = 'CA'
        elif c_score < a_score or c_score < b_score:
            winner = 'AB'

    if prev_winner != winner:
        change_cnts += 1
        prev_winner, winner = winner, ''

print(change_cnts)
N = int(input())
changes = []
for _ in range(N):
    c, s = input().split()
    ch_score = int(s)
    changes.append([c, ch_score])

a_score, b_score = 0, 0
change_cnts = 0
prev_winner, winner = '', ''
for ch_idx, (player, ch_score) in enumerate(changes):
    if player == 'A':
        a_score += ch_score
    elif player == 'B':
        b_score += ch_score

    if ch_idx != 0:
        if player == 'A':
            a_score += ch_score
        elif player == 'B':
            b_score += ch_score

        if a_score > b_score:
            winner = 'A'
        elif a_score < b_score:
            winner = 'B'
        else:
            change_cnts += 1

        if prev_winner != winner:
            change_cnts += 1
            prev_winner, winner = winner, ''
    else:
        if player == 'A':
            a_score += ch_score
            prev_winner, winner = player, player
        elif player == 'B':
            b_score += ch_score
            prev_winner, winner = player, player

        if len(changes) > 1:
            change_cnts += 1

print(change_cnts)
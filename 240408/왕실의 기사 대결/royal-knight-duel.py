from collections import deque

L, N, Q = map(int, input().split())
fix_board = [list(map(int, input().split())) for _ in range(L)]

# 입력받은 기사의 정보
knights = [0]
# 몇 번째 기사의 방패가 있는지 저장
shield = [[0] * L for _ in range(L)]
move_dirs = {0: (-1, 0), 1: (0, 1), 2:(1, 0), 3: (0, -1)}
chess = {}
for knight_num in range(1, N + 1):
    r, c, h, w, k = map(int, input().split())
    chess[knight_num] = []
    for row in range(h):
        for col in range(w):
            shield[r - 1 + row][c - 1 + col] = knight_num
            chess[knight_num].append([r - 1 + row, c - 1 + col])
    knights.append([r - 1, c - 1, h, w, k])

damages = [0 for _ in range(N + 1)]
for _ in range(Q):
    mv_knight, mv_dir = map(int, input().split())

    if knights[mv_knight] == 0:
        continue

    wall = 0
    # 움직일 기사
    r, c, _, _, _ = knights[mv_knight]
    que = deque([[r, c]])
    check = [[0] * L for _ in range(L)]
    check[r][c] = 1

    # 몇 번째 방패가 이동하는지
    move_shield = [0 for _ in range(N + 1)]
    move_shield[mv_knight] = 1

    while que:
        r, c = que.popleft()
        for d_dir, (dr, dc) in move_dirs.items():
            mr, mc = r + dr, c + dc
            if 0 <= mr < L and 0 <= mc < L:
                if check[mr][mc] == 0:
                    if shield[mr][mc] == shield[r][c]:
                        check[mr][mc] = 1
                        que.append([mr, mc])

            # mv_dir방향으로 이동할 때 다른 방패를 밀어내는지, 다음 칸이 벽인지 확인
            if d_dir == mv_dir:
                if 0 <= mr < L and 0 <= mc < L:
                    if check[mr][mc] == 0:
                        if shield[mr][mc] > 0 and shield[mr][mc] != shield[r][c]:
                            check[mr][mc] = 1
                            que.append([mr, mc])
                            move_shield[shield[mr][mc]] = 1

                        if fix_board[mr][mc] == 2:
                            wall = 1
                            break
                else:
                    wall = 1
                    break

        if wall == 1:
            break

    # 기사 이동
    # tmp_shield에 방패를 먼저 이동시키고 나중에 shield를 수정
    tmp_shield = [[0] * L for _ in range(L)]
    if wall == 0:
        for knight_num in range(1, N + 1):
            if move_shield[knight_num] == 1:
                # chess 수정을 위한 임시 리스트
                tmp_chess = []
                for r, c in chess[knight_num]:
                    mr, mc = r + move_dirs[mv_dir][0], c + move_dirs[mv_dir][1]
                    tmp_shield[mr][mc] = knight_num
                    tmp_chess.append([mr, mc])

                # knight_num번째 기사의 chess와 knight에서 좌표값 수정
                chess[knight_num] = tmp_chess
                knights[knight_num][:2] = chess[knight_num][0]

        # 방패가 있는 좌표 수정
        for r in range(L):
            for c in range(L):
                if shield[r][c] > 0 and tmp_shield[r][c] == 0:
                    if move_shield[shield[r][c]] == 1:
                        shield[r][c] = 0
                if tmp_shield[r][c] > 0:
                    shield[r][c] = tmp_shield[r][c]

        # 함정 확인
        for r in range(L):
            for c in range(L):
                if fix_board[r][c] == 1 and shield[r][c] > 0:
                    knight = shield[r][c]
                    # 밀어내는 기사는 제외하고 밀려난 기사만 피해를 받음
                    if move_shield[knight] == 1 and knight != mv_knight:
                        if knights[knight] != 0:
                            knights[knight][-1] -= 1
                            damages[knight] += 1
                            # 체력이 0이 되면 knight, damage를 0으로 초기화
                            if knights[knight][-1] == 0:
                                for rr, cc in chess[knight]:
                                    shield[rr][cc] = 0
                                knights[knight] = 0
                                damages[knight] = 0
                                continue

print(sum(damages))
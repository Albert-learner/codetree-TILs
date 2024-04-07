N, M, P, C, D = map(int, input().split())
visited = [[0] * N for _ in range(N)]
rdp_r, rdp_c = map(lambda x: int(x) - 1, input().split())
visited[rdp_r][rdp_c] = -1

santa_score = [0] * (P + 1)
alive = [1] * (P + 1)
alive[0] = 0
wakeup_turns = [1] * (P + 1)

Santas = [[N] * 2 for _ in range(P + 1)]
for _ in range(1, P + 1):
    s_num, r, c = map(int, input().split())
    Santas[s_num] = [r - 1, c - 1]
    visited[r - 1][c - 1] = N

def move_santa(cur_santa, sr, sc, dr, dc, mul):
    # cur_santa번 산타를 sr, sc에서 dr, dc방향으로 mul칸 이동
    q = [(cur_santa, sr, sc, mul)]

    while q:
        cur_santa, cr, cc, mul = q.pop(0)
        # 진행방향 mul칸만큼 이동시켜서 범위내이고 산타있으면 q삽입 / 범위밖 처리
        mr, mc = cr + dr * mul, cc + dc * mul
        # 범위 내 산타 O, X
        if 0 <= mr < N and 0 <= mc < N:
            # 빈 칸 => 이동처리
            if visited[mr][mc] == 0:
                visited[mr][mc] = cur_santa
                Santas[cur_santa] = [mr, mc]
                return
            else:
                q.append((visited[mr][mc], mr, mc, 1))
                visited[mr][mc] = cur_santa
                Santas[cur_santa] = [mr, mc]
        else:
            alive[cur_santa] = 0
            return

for turn in range(1, M + 1):
    # 0. 모두 탈락 시(alive 모두 0) => break
    if alive.count(1) == 0:
        break

    # 1-1. 루돌프 이동: 가장 가까운 산타 찾기
    min_dst = N ** 2
    for santa in range(1, P + 1):
        # 탈락한 산타 => skip
        if alive[santa] == 0:
            continue

        sr, sc = Santas[santa]
        dst = (rdp_r - sr) ** 2 + (rdp_c - sc) ** 2
        if dst < min_dst:
            min_dst = dst
            nrt_santas = [(sr, sc, santa)]
        elif dst == min_dst:
            nrt_santas.append((sr, sc, santa))

    # 행 큰 > 열 큰
    nrt_santas.sort(reverse=True)
    nrt_sr, nrt_sc, nrt_santa = nrt_santas[0]

    # 1-2. 대상 산타(루돌프와 가장 가까운) 방향으로 루돌프 이동
    rdr, rdc = 0, 0
    # 산타가 작은값 좌표 => -1방향으로 이동
    if rdp_r > nrt_sr:
        rdr = -1
    elif rdp_r < nrt_sr:
        rdr = 1

    if rdp_c > nrt_sc:
        rdc = -1
    elif rdp_c < nrt_sc:
        rdc = 1

    # 루돌프 현재자리 지우기
    visited[rdp_r][rdp_c] = 0
    # 루돌프 이동
    rdp_r, rdp_c = rdp_r + rdr, rdp_c + rdc
    # 이동한 자리에 표시
    visited[rdp_r][rdp_c] = -1

    # 1-3. 루돌프와 산타가 충돌한 경우 산타가 밀리는 처리
    if (rdp_r, rdp_c) == (nrt_sr, nrt_sc):
        santa_score[nrt_santa] += C
        wakeup_turns[nrt_santa] = turn + 2
        move_santa(nrt_santa, nrt_sr, nrt_sc, rdr, rdc, C)

    # 2-1. 순서대로 산타이동: 기절하지 않은 경우(산타 차례 <= turn)
    for santa in range(1, P + 1):
        # 탈락한 경우 skip
        if alive[santa] == 0:
            continue

        # 깨어날 차례가 아직 안된 경우
        if wakeup_turns[santa] > turn:
            continue

        sr, sc = Santas[santa]
        min_dst = (rdp_r - sr) ** 2 + (rdp_c - sc) ** 2
        moves_lst = []
        # 상우하좌 순으로 최소거리 찾기
        for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            mr, mc = sr + dr, sc + dc
            dst = (mr - rdp_r) ** 2 + (mc - rdp_c) ** 2
            if 0 <= mr < N and 0 <= mc < N and visited[mr][mc] <= 0 and min_dst > dst:
                min_dst = dst
                moves_lst.append((mr, mc, dr, dc))

        # 이동할 위치 없음
        if len(moves_lst) == 0:
            continue

        # 마지막에 추가된 더 짧은 거리
        mr, mc, dr, dc = moves_lst[-1]

        # 2-2. 루돌프와 충돌 시 처리
        if (rdp_r, rdp_c) == (mr, mc):
            santa_score[santa] += D
            wakeup_turns[santa] = turn + 2
            visited[sr][sc] = 0
            move_santa(santa, mr, mc, -dr, -dc, D)
        else:
            visited[sr][sc] = 0
            visited[mr][mc] = santa
            Santas[santa] = [mr, mc]

    # 3. 점수획득: alive산타는 +1점
    for santa in range(1, P + 1):
        if alive[santa] == 1:
            santa_score[santa] += 1

print(*santa_score[1:])
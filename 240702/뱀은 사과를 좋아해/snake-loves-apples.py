from collections import deque

# 범위 체크 함수
def in_range(x, y, N):
    return 0 <= x < N and 0 <= y < N

# 시뮬레이션 함수
def simulate(board, dir_board, head, tail, dir_head, dist, N):
    T = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    
    for _ in range(dist):
        T += 1
        dir_board[head[0]][head[1]] = dir_head
        
        nx_head = head[0] + dx[dir_head]
        ny_head = head[1] + dy[dir_head]
        
        # 다음 위치가 격자 밖이면 게임오버
        if not in_range(nx_head, ny_head, N):
            return True, T, head, tail, board, dir_board
        
        # 다음 위치가 뱀의 몸통이면 게임오버 (꼬리는 제외)
        if board[nx_head][ny_head] == 1 and (nx_head != tail[0] or ny_head != tail[1]):
            return True, T, head, tail, board, dir_board
        
        # 다음 위치가 사과라면
        if board[nx_head][ny_head] == 2:
            head = [nx_head, ny_head]
            board[head[0]][head[1]] = 1
            continue
        
        # 빈 공간에 이동했다면
        head = [nx_head, ny_head]
        board[head[0]][head[1]] = 1
        
        # 꼬리를 dir_board를 보고 이동
        dir_tail = dir_board[tail[0]][tail[1]]
        board[tail[0]][tail[1]] = 0
        tail[0] += dx[dir_tail]
        tail[1] += dy[dir_tail]
    
    return False, T, head, tail, board, dir_board

# 메인 함수
def main():
    N, M, K = map(int, input().split())
    
    board = [[0] * N for _ in range(N)]
    dir_board = [[0] * N for _ in range(N)]
    
    for _ in range(M):
        x, y = map(int, input().split())
        board[x-1][y-1] = 2  # 사과 위치 설정
    
    board[0][0] = 1  # 초기 뱀 위치 설정
    head = [0, 0]
    tail = [0, 0]
    T_total = 0
    char_to_int = {'U': 0, 'D': 1, 'R': 2, 'L': 3}
    
    game_over = False
    for _ in range(K):
        if game_over:
            break
        comm, dist = input().split()
        dist = int(dist)
        game_over, T, head, tail, board, dir_board = simulate(board, dir_board, head, tail, char_to_int[comm], dist, N)
        T_total += T
    
    print(T_total)

if __name__ == "__main__":
    main()
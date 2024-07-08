import sys

# 방향을 나타내는 배열
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def parse_key(key):
    # 좌표 문자열을 분리하여 리스트로 반환
    return list(map(int, key.split(',')))

def make_key(x, y):
    # 좌표를 문자열로 변환하여 키로 사용
    return f"{x},{y}"

def turn_direc(direc):
    # 방향을 반대로 전환
    if direc == 0:
        return 1
    elif direc == 1:
        return 0
    elif direc == 2:
        return 3
    else:
        return 2

def is_range(x, y, n):
    # 좌표가 유효한 범위인지 확인
    return 0 <= x < n and 0 <= y < n

def get_direc(direc):
    # 방향을 숫자로 변환
    if direc == 'U':
        return 0
    elif direc == 'D':
        return 1
    elif direc == 'L':
        return 2
    else:
        return 3

def main():
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []

    for _ in range(t):
        n = int(data[idx])
        m = int(data[idx + 1])
        idx += 2

        # 초기 지도 생성
        map_dict = {}

        for _ in range(m):
            r = int(data[idx]) - 1
            c = int(data[idx + 1]) - 1
            direc = get_direc(data[idx + 2])
            idx += 3

            map_dict[make_key(c, r)] = direc

        sec = 0
        while sec <= 2 * n:
            sec += 1
            memo = [[0] * n for _ in range(n)]
            renew_map = {}

            for key in map_dict.keys():
                pos = parse_key(key)
                x, y = pos
                direc = map_dict[key]

                nx = x + dx[direc]
                ny = y + dy[direc]

                if is_range(nx, ny, n):
                    memo[ny][nx] += 1

                    if memo[ny][nx] > 1:
                        renew_map.pop(make_key(nx, ny), None)
                    else:
                        renew_map[make_key(nx, ny)] = direc
                else:
                    memo[y][x] += 1

                    if memo[y][x] > 1:
                        renew_map.pop(make_key(x, y), None)
                    else:
                        renew_map[make_key(x, y)] = turn_direc(direc)

            map_dict = renew_map

        ans = len(map_dict)
        results.append(str(ans))

    print("\n".join(results))

if __name__ == "__main__":
    main()
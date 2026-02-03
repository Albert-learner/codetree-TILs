import sys
import heapq

def main():
    input = sys.stdin.readline

    n = int(input().strip())
    pq = []

    # (start, end) 기준으로 최소힙 구성 (Java compareTo와 동일: s 오름차순, s 같으면 e 오름차순)
    for _ in range(n):
        s, e = map(int, input().split())
        heapq.heappush(pq, (s, e))

    current_s, current_e = heapq.heappop(pq)
    res = 1

    while pq:
        next_s, next_e = heapq.heappop(pq)

        # 마지막으로 고른 것보다 더 빨리 끝낼 수 있으면 교체
        if next_e < current_e:
            current_s, current_e = next_s, next_e
            continue

        # 마지막으로 고른 것 이후에 시작 가능하면 추가로 선택
        if next_s >= current_e:
            res += 1
            current_s, current_e = next_s, next_e

    print(res)

if __name__ == "__main__":
    main()

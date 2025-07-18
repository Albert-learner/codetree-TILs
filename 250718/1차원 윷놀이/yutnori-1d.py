from functools import lru_cache

def calc(pieces, m):
    return sum(1 for p in pieces if p >= m)

def solve(n, m, k, nums):
    @lru_cache(maxsize=None)
    def backtrack(cnt, *pieces):  # pieces: unpacked as tuple
        current_score = sum(1 for p in pieces if p >= m)
        if cnt == n:
            return current_score

        max_score = current_score
        for i in range(k):
            if pieces[i] >= m:
                continue

            # 리스트로 복사하여 이동 시뮬레이션
            next_pieces = list(pieces)
            next_pieces[i] += nums[cnt]
            score = backtrack(cnt + 1, *next_pieces)
            max_score = max(max_score, score)

        return max_score

    # 초기 상태: 모든 말은 위치 1
    return backtrack(0, *([1] * k))

# 입력
n, m, k = map(int, input().split())
nums = list(map(int, input().split()))

# 실행
print(solve(n, m, k, nums))
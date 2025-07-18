def calc(pieces, m):
    return sum(1 for p in pieces if p >= m)

def find_max(cnt, n, m, k, nums, pieces):
    # 재귀 진입 시 항상 정답 갱신
    current_score = calc(pieces, m)
    
    if cnt == n:
        return current_score

    max_score = current_score
    has_moved = False

    for i in range(k):
        if pieces[i] >= m:
            continue

        has_moved = True
        pieces[i] += nums[cnt]
        score = find_max(cnt + 1, n, m, k, nums, pieces)
        max_score = max(max_score, score)
        pieces[i] -= nums[cnt]

    return max_score

# 입력 처리
n, m, k = map(int, input().split())
nums = list(map(int, input().split()))
pieces = [1] * k

# 실행
answer = find_max(0, n, m, k, nums, pieces)
print(answer)
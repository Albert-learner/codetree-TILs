def calc(horse_status, m):
    return sum(pos >= m for pos in horse_status)

def backtracking(curr_idx, horse_status, command, n, m, k):
    if curr_idx == n:
        return calc(horse_status, m)

    max_score = 0
    for i in range(k):
        if horse_status[i] >= m:
            continue

        # 말 하나 이동
        horse_status[i] += command[curr_idx]
        score = backtracking(curr_idx + 1, horse_status, command, n, m, k)
        max_score = max(max_score, score)
        horse_status[i] -= command[curr_idx]  # 복원

    return max_score

# 입력
n, m, k = map(int, input().split())
command = list(map(int, input().split()))
horse_status = [1] * k

# 실행
result = backtracking(0, horse_status, command, n, m, k)
print(result)
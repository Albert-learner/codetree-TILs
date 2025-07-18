def backtracking(curr_idx, horse_status, command, n, m, k):
    if curr_idx == n:
        return sum(1 for val in horse_status if val >= m)

    max_score = 0
    for i in range(k):
        if horse_status[i] >= m:
            continue

        # 말 이동
        horse_status[i] += command[curr_idx]
        score = backtracking(curr_idx + 1, horse_status, command, n, m, k)
        max_score = max(max_score, score)
        horse_status[i] -= command[curr_idx]  # 백트래킹

    return max_score

# 입력 및 실행
n, m, k = map(int, input().split())
command = list(map(int, input().split()))
horse_status = [1] * k

result = backtracking(0, horse_status, command, n, m, k)
print(result)
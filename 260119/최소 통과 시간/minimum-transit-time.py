def can_pass(mid, times, n):
    total = sum(mid // time for time in times)
    return total >= n

def min_pass_time(n, m, times):
    left, right = 0, max(times) * n
    answer = right
    
    while left <= right:
        mid = (left + right) // 2
        if can_pass(mid, times, n):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    return answer

# 입력 받기
n, m = map(int, input().split())
times = [int(input()) for _ in range(m)]

# 결과 출력
print(min_pass_time(n, m, times))
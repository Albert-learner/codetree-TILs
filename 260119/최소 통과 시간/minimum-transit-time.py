n, m = map(int, input().split())
arr = [int(input()) for _ in range(m)]

# Please write your code here.
def can_pass(mid, times, n):
    total = sum(mid / time for time in times)
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

print(min_pass_time(n, m, arr))
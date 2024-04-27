N, K = map(int, input().split())
stones = list(map(int, input().split()))

def jump_possible(min_val):
    cnts = 0
    available_stones = [0] * 100
    for i in range(N):
        if stones[i] <= min_val:
            available_stones[cnts] = i
            cnts += 1

    for i in range(1, cnts):
        if available_stones[i] - available_stones[i - 1] > K:
            return False

    return True


maxmin_cst = float("inf")
for stone in range(100, max(stones[0], stones[N - 1]) - 1, -1):
    if jump_possible(stone):
        maxmin_cst = min(maxmin_cst, stone)

print(maxmin_cst)
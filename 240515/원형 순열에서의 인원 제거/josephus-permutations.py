from collections import deque

def josephus_permutation(N, K):
    queue = deque(range(1, N + 1))
    result = []

    while queue:
        for _ in range(K - 1):
            queue.append(queue.popleft())
        result.append(queue.popleft())

    return result

N, K = map(int, input().split())

print(*josephus_permutation(N, K))
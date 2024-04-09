N, K, T = input().split()
N, K = int(N), int(K)
words = [input() for _ in range(N)]

satisfies = []
for word in words:
    if word.startswith(T):
        satisfies.append(word)

satisfies.sort()
print(satisfies[K - 1])
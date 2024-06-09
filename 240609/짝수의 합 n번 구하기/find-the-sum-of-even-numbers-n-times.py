N = int(input())
pairs = [map(int, input().split()) for _ in range(N)]

for a, b in pairs:
    eval_sum = 0
    for n in range(a, b + 1):
        if n % 2 == 0:
            eval_sum += n

    print(eval_sum)
n = int(input())
arr = list(map(int, input().split()))

INF = 10 ** 9
best = INF

def solve(start_press_2: bool) -> int:
    a = arr[:]
    cnt = 0

    def press(i): 
        nonlocal cnt
        cnt += 1
        if i - 1 >= 1:
            a[i - 2] ^= 1
        a[i - 1] ^= 1
        if i + 1 <= n:
            a[i] ^= 1

    if n >= 2 and start_press_2:
        press(2)

    for i in range(3, n + 1):
        if a[i - 3] == 0:  
            press(i)

    if n == 1:
        return 0 if a[0] == 1 else INF 
    if n == 2:
        return cnt if (a[0] == 1 and a[1] == 1) else INF

    return cnt if (a[n - 2] == 1 and a[n - 1] == 1) else INF


best = min(solve(False), solve(True))
print(-1 if best == INF else best)

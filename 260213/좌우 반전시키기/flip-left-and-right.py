n = int(input())
arr = list(map(int, input().split()))

INF = 10 ** 9
best = INF

def solve():
    a = arr[:]
    cnt = 0

    def press(i): 
        nonlocal cnt
        cnt += 1
        if i - 1 >= 0:
            a[i - 1] ^= 1
        a[i] ^= 1
        if i + 1 <= n:
            a[i + 1] ^= 1

    if n == 1:
        return 0 if a[0] == 1 else -1

    if a[0] == 0:
        press(1)

    for i in range(2, n):
        if a[i - 1] == 0:  
            press(i)

    return cnt if all(x == 1 for x in a) else -1


print(solve())

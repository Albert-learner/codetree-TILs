N = int(input())
pairs = [map(int, input().split()) for _ in range(N)]

for a, b in pairs:
    mul_cst = 1
    for n in range(a, b + 1):
        mul_cst *= n
    print(mul_cst)
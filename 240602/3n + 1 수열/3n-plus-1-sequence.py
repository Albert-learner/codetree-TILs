N = int(input())

cnts = 0
while N != 1:
    if N % 2 == 0:
        N //= 2
    else:
        N *= 3
        N += 1

    cnts += 1
    
print(cnts)
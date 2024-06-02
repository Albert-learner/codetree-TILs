cnts = 0

while cnts < 3:
    N = int(input())

    if N % 2 == 1:
        continue
    else:
        print(N // 2)
        cnts += 1
M = int(input())
n_lst = [int(input()) for _ in range(M)]

for n in n_lst:
    cnts = 0
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n *= 3
            n += 1
        
        cnts += 1
    
    print(cnts)
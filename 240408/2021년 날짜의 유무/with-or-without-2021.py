M, D = map(int, input().split())

if M in range(1, 13):
    if M != 2:
        if M in [1, 3, 5, 7, 8, 10, 12]:
            if D in range(1, 32):
                print("Yes")
            else:
                print("No")
        else:
            if D in range(1, 31):
                print("Yes")
            else:
                print("No")
    else:
        if D in range(1, 29):
            print("Yes")
        else:
            print("No")
else:
    print("No")
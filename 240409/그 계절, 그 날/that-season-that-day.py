Y, M, D = map(int, input().split())

if Y in range(1, 3001):
    if not((Y % 4 == 0 and Y % 100 != 0) or Y % 400 == 0):
        if M in [12, 1, 2]:
            if M in [12, 1]:
                if D in range(1, 32):
                    print("Winter")
                else:
                    print(-1)
            else:
                if D in range(1, 31):
                    print("Winter")
                else:
                    print(-1)
        elif M in [3, 4, 5]:
            if M in [3, 5]:
                if D in range(1, 32):
                    print("Spring")
                else:
                    print(-1)
            else:
                if D in range(1, 31):
                    print("Spring")
                else:
                    print(-1)
        elif M in [6, 7, 8]:
            if M in [7, 8]:
                if D in range(1, 32):
                    print("Summer")
                else:
                    print(-1)
            else:
                if D in range(1, 31):
                    print("Summer")
                else:
                    print(-1)
        elif M in [9, 10, 11]:
            if M == 10:
                if D in range(1, 32):
                    print("Fall")
                else:
                    print(-1)
            else:
                if D in range(1, 31):
                    print("Fall")
                else:
                    print(-1)
        else:
            print(-1)
    else:
        if M != 2:
            if M in [12, 1]:
                if D in range(1, 32):
                    print("Winter")
                else:
                    print(-1)
            elif M in [3, 4, 5]:
                if M in [3, 5]:
                    if D in range(1, 32):
                        print("Spring")
                    else:
                        print(-1)
                else:
                    if D in range(1, 31):
                        print("Spring")
                    else:
                        print(-1)
            elif M in [6, 7, 8]:
                if M in [7, 8]:
                    if D in range(1, 32):
                        print("Summer")
                    else:
                        print(-1)
                else:
                    if D in range(1, 31):
                        print("Summer")
                    else:
                        print(-1)
            elif M in [9, 10, 11]:
                if M == 10:
                    if D in range(1, 32):
                        print("Fall")
                    else:
                        print(-1)
                else:
                    if D in range(1, 31):
                        print("Fall")
                    else:
                        print(-1)
        else:
            if D in range(1, 30):
                print("Winter")
else:
    print(-1)
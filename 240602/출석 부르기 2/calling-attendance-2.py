while True:
    n = int(input())
    
    if n not in [1, 2, 3, 4]:
        print("Vacancy")
        break
    elif n == 1:
        print("John")
    elif n == 2:
        print("Tom")
    elif n == 3:
        print("Paul")
    elif n == 4:
        print("Sam")
N = int(input())

def print_str(N):
    if N == 0:
        return 

    print_str(N - 1)
    print("HelloWorld")

print_str(N)
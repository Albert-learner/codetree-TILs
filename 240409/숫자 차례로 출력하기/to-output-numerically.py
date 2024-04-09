N = int(input())

def print_number(N):
    if N == 0:
        return

    print_number(N - 1)
    print(N, end = ' ')

def print_rev_number(N):
    if N == 0:
        return

    print(N, end = ' ')
    print_rev_number(N - 1)

print_number(N)
print()
print_rev_number(N)
N = int(input())

# Please write your code here.
def fibonacci(n):
    a, b = 0, 1

    for _ in range(n):
        a, b = b, a + b

    return a

print(fibonacci(N))
n = int(input())

print("book" if 3000 <= n <= 10000 else "mask" if 1000 <= n < 3000 else "pen" if 500 <= n < 1000 else "no")
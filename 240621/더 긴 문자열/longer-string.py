first, second = input().split()

if len(first) > len(second):
    print(first, len(first))
elif len(first) < len(second):
    print(second, len(second))
else:
    print("same")
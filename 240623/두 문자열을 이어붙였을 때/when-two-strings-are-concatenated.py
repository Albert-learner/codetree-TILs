first = input()
second = input()

front, end = first + second, second + first

print("true" if front == end else "false")
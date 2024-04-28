x1, y1, x2, y2 = map(int, input().split())
a1, b1, a2, b2 = map(int, input().split())

first_rectangle = [(x1, y1), (x1, y2), (x2, y1), (x2, y2)]
second_rectangle = [(a1, b1), (a1, b2), (a2, b1), (a2, b2)]

if (a1 in range(x1, x2 + 1) and b1 in range(y1, y2 + 1)) or (a1 in range(x1, x2 + 1) and b2 in range(y1, y2 + 1)) or (a2 in range(x1, x2 + 1) and b1 in range(y1, y2 + 1)) or (a2 in range(x1, x2 + 1) and b2 in range(y1, y2 + 1)):
    print("overlapping")
else:
    print("nonoverlapping")
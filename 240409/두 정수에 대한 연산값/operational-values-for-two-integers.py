A, B = map(int, input().split())

if A > B:
    A += 25
    B *= 2
else:
    B += 25
    A *= 2

print(A, B)
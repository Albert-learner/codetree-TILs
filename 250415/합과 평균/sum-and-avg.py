A, B = map(int, input().split())

avg = round((A + B) / 2, 1)

print("{} {:.1f}".format(A + B, avg))
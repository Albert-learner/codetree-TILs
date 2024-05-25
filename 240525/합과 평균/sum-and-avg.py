a, b = map(int, input().split())

print(sum([a, b]), "{:.1f}".format(round(sum([a, b]) / 2, 1)))
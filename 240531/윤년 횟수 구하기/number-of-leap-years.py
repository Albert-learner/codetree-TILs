N = int(input())

cnts = 0
for i in range(1, N + 1):
    if i % 4 == 0:
        if i % 100 == 0 and i % 400 != 0:
            continue
        else:
            cnts += 1

print(cnts)
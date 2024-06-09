scores = list(map(float, input().split()))

print(round(sum(scores) / len(scores), 1))
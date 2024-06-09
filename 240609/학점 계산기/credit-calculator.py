N = int(input())
scores = list(map(float, input().split()))

avg = round(sum(scores) / len(scores), 1)
print(avg)
if avg >= 4.0:
    print("Perfect")
elif 3.0 <= avg < 4.0:
    print("Good")
else:
    print("Poor")
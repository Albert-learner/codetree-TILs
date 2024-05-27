left = float(input())
right = float(input())

print("High" if left >= 1.0 and right >= 1.0 else "Middle" if left >= 0.5 and right >= 0.5 else "Low")
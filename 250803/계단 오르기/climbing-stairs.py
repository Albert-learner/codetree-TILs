n = int(input())

# Please write your code here.
climb_stairs = [0, 1, 1] + [0] * 1000

for i in range(3, n):
    climb_stairs[i] = climb_stairs[i - 2] + climb_stairs[i - 3]

print(climb_stairs[n - 1])
n = int(input())

# Please write your code here.
climb_stairs = [0] * (n + 1)
climb_stairs[0], climb_stairs[1], climb_stairs[2] = 0, 1, 1

for i in range(3, n + 1):
    climb_stairs[i] = climb_stairs[i - 2] + climb_stairs[i - 3]

print(climb_stairs[n - 1] % 10007)
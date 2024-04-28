N = int(input())
hills = [int(input()) for _ in range(N)]
hills.sort()

costs = 0
min_pos, max_pos = 0, -1
while hills[max_pos] - hills[min_pos] > 17:
    min_pos += 1
    max_pos -= 1

for i in range(min_pos):
    costs += (hills[min_pos] - hills[i]) ** 2

for i in range(-1, max_pos, -1):
    costs += (hills[max_pos] - hills[i]) ** 2
print(costs)
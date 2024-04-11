N, M = map(int, input().split())
robot_A, robot_B = [0], [0]

cur_a, cur_b = 0, 0
for _ in range(N):
    size, mv_dir = input().split()
    size = int(size)

    if mv_dir == 'R':
        for i in range(cur_a + 1, cur_a + size + 1):
            robot_A.append(i)
        cur_a += size
    else:
        for i in range(cur_a - 1, cur_a - size - 1, -1):
            robot_A.append(i)
        cur_a -= size

for _ in range(M):
    size, mv_dir = input().split()
    size = int(size)

    if mv_dir == 'R':
        for i in range(cur_b + 1, cur_b + size + 1):
            robot_B.append(i)
        cur_b += size
    else:
        for i in range(cur_b - 1, cur_b - size - 1, -1):
            robot_B.append(i)
        cur_b -= size

diff = abs(len(robot_A) - len(robot_B))
if len(robot_A) > len(robot_B):
    for _ in range(diff):
        robot_B.append(robot_B[-1])
else:
    for _ in range(diff):
        robot_A.append(robot_A[-1])

answer = 0
for idx in range(1, len(robot_A)):
    if robot_A[idx] == robot_B[idx] and robot_A[idx - 1] != robot_B[idx - 1]:
        answer += 1

print(answer)
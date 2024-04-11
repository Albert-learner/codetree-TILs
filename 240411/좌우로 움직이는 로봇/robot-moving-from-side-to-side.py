# 내 풀이
N, M = map(int, input().split())
robot_A, robot_B = [0], [0]

cur_a, cur_b = 0, 0
for _ in range(N):
    size, mv_dir = input().split()
    size = int(size)

    if mv_dir == 'R':
        for i in range(robot_A[-1] + 1, robot_A[-1] + size + 1):
            robot_A.append(i)
        cur_a += size
    else:
        for i in range(robot_A[-1] - 1, robot_A[-1] - size - 1, -1):
            robot_A.append(i)
        cur_a -= size

for _ in range(M):
    size, mv_dir = input().split()
    size = int(size)

    if mv_dir == 'R':
        for i in range(robot_B[-1] + 1, robot_B[-1] + size + 1):
            robot_B.append(i)
        cur_b += size
    else:
        for i in range(robot_B[-1] - 1, robot_B[-1] - size - 1, -1):
            robot_B.append(i)
        cur_b -= size

robot_A = robot_A[1:]
robot_B = robot_B[1:]

diff = abs(len(robot_A) - len(robot_B))
if len(robot_A) > len(robot_B):
    for _ in range(diff):
        robot_B.append(robot_B[-1])
else:
    for _ in range(diff):
        robot_A.append(robot_A[-1])

answer = 0
for (a_elem_idx, a_elem), (b_elem_idx, b_elem) in zip(enumerate(robot_A), enumerate(robot_B)):
    if a_elem == b_elem and robot_A[a_elem_idx - 1] != robot_B[b_elem_idx - 1]:
        answer += 1

print(answer)
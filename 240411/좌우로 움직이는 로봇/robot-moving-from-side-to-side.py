N, M = map(int, input().split())
robot_A, robot_B = [], []

cur_a, cur_b = 0, 0
for _ in range(N):
    size, mv_dir = input().split()
    size = int(size)

    if mv_dir == 'R':
        for i in range(cur_a, cur_a + size):
            robot_A.append(i)
        cur_a += size 
    else:
        for i in range(cur_a, cur_a - size, -1):
            robot_A.append(i)
        cur_a -= size

for _ in range(M):
    size, mv_dir = input().split()
    size = int(size)

    if mv_dir == 'R':
        for i in range(cur_b, cur_b + size):
            robot_B.append(i)
        cur_b += size
    else:
        for i in range(cur_b, cur_b - size, -1):
            robot_B.append(i)
        cur_b -= size

answer = 0
for (a_elem_idx, a_elem), (b_elem_idx, b_elem) in zip(enumerate(robot_A[1:]), enumerate(robot_B[1:])):
    if a_elem == b_elem and robot_A[a_elem_idx - 1] != robot_B[b_elem_idx - 1]:
        answer += 1

print(answer + 1)
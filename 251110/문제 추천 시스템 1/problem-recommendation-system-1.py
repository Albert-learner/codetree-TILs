from sortedcontainers import SortedSet

# 변수 선언 및 입력:
n = int(input())
problems = SortedSet()
for _ in range(n):
    p, l = tuple(map(int, input().split()))

    # 주어진 문제를 treeset에 넣어줍니다.
    problems.add((l, p))

m = int(input())
# m개의 명령을 수행합니다.
for _ in range(m):
    command = input()

    if command.startswith("ad"):
        _, p, l = command.split()
        p, l = int(p), int(l)

        # 문제를 추가합니다.
        problems.add((l, p))
    elif command.startswith("sv"):
        _, p, l = command.split()
        p, l = int(p), int(l)

        # 문제를 제거힙니다.
        problems.remove((l, p))
    else:
        x = int(command.split()[1])

        # x가 1이면 난이도가 가장 높은 문제의 번호를 출력합니다.
        if x == 1:
            _, p = problems[-1]
            print(p)
        # x가 -1이면 난이도가 가장 낮은 문제의 번호를 출력합니다.
        else:
            _, p = problems[0]
            print(p)

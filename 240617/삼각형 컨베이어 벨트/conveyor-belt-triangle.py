N, T = map(int, input().split())
belt = [list(map(int, input().split())) for _ in range(3)]
first, second, third = belt[0], belt[1], belt[2]

while T > 0:
    second.insert(0, first.pop())
    third.insert(0, second.pop())
    first.insert(0, third.pop())
    T -= 1

print(*first)
print(*second)
print(*third)
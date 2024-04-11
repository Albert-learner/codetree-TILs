N, K, P, T = map(int, input().split())
handshakes = sorted([list(map(int, input().split())) for _ in range(T)])

people = [0] * N
spread = [K for _ in range(N)]
people[P - 1] = 1

for _, x, y in handshakes:
    if (x == P or people[x - 1] == 1) and (y == P or people[y - 1] == 1):
        spread[x - 1] -= 1
        spread[y - 1] -= 1
    elif (x == P or people[x - 1] == 1) and spread[x - 1] > 0:
        people[y - 1] = 1
        spread[x - 1] -= 1
    elif (y == P or people[y - 1] == 1) and spread[y - 1] > 0:
        people[x - 1] = 1
        spread[y - 1] -= 1

print("".join(map(str, people)))
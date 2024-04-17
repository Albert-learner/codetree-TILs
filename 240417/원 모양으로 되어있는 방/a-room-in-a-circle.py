import sys

MIN_DST = sys.maxsize

N = int(input())
people = [int(input()) for _ in range(N)]


for i in range(N):
    sum_dst = 0
    for j in range(N):
        dst = (j + N - i) % N
        sum_dst += dst * people[j]

    MIN_DST = min(MIN_DST, sum_dst)

print(MIN_DST)
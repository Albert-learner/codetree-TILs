n = int(input())
T = input()
P = input()

# Please write your code here.
same_cnts = 0
for i in range(n):
    P = P[-1] + P[:-1]
    if P == T:
        same_cnts += 1

print(same_cnts)
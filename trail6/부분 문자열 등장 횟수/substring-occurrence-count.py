T = input()
P = input()

# Please write your code here.
n, m = len(T), len(P)

if P not in T:
    print(0)
    exit(0)

f = [0] * (m + 1)

text = '#' + T
pattern = '#' + P

f[0] = -1
sub_cnts = 0
for i in range(1, m + 1):
    j = f[i - 1]
    while j >= 0 and pattern[j + 1] != pattern[i]:
        j = f[j]
    f[i] = j + 1

j = 0
for i in range(1, n + 1):
    while j >= 0 and pattern[j + 1] != text[i]:
        j = f[i]
    j += 1

    if j == m:
        sub_cnts += 1
        j = f[j]

print(sub_cnts)
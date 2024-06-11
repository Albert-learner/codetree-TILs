a, b = map(int, input().split())

if a < b:
    a, b = b, a

rests = []
rests_cntr = {n: 0 for n in range(b)}
while a > 1:
    rests.append(a % b)
    a //= b

for rest in rests:
    if rest in rests_cntr:
        rests_cntr[rest] += 1

print(sum([cnts ** 2 for cnts in rests_cntr.values()]))
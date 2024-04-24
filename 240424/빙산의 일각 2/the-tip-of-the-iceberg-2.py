N = int(input())

ice_bergs = [0] * 100

for i in range(N):
    ice_bergs[i] = int(input())

max_height = max(ice_bergs)
max_cnts = 0
for i in range(max_height):
    tmp_ice_bergs = ice_bergs[:N]

    for j in range(N):
        if tmp_ice_bergs[j] - i < 0:
            tmp_ice_bergs[j] = 0
        else:
            tmp_ice_bergs[j] -= i

    cnts, bit = 0, 0
    for chk in range(N):
        if tmp_ice_bergs[chk] != 0:
            bit = 1

        if bit == 1 and tmp_ice_bergs[chk] == 0:
            bit = 0
            cnts += 1

        if bit == 1 and chk == N - 1:
            cnts += 1

    max_cnts = max(max_cnts, cnts)

print(max_cnts)
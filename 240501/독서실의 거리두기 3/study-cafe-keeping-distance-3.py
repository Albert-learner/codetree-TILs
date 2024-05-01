N = int(input())
seats = list(map(int, input()))

def get_min_diff(lst):
    cnts = 0
    diffs = []
    for j in range(len(lst)):
        if lst[j] == 1:
            diffs.append(cnts)
            cnts = 0

        cnts += 1

    return min(diffs[1::])
    

max_dst = -1
for i in range(N):
    if seats[i] == 0:
        seats[i] = 1

        max_dst = max(max_dst, get_min_diff(seats))

        seats[i] = 0

print(max_dst)
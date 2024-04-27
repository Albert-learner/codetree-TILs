N = int(input())
seats = list(input())

def get_dist():
    min_num = 21e8
    last_flag, cur_flag = -1, -1
    for i in range(N):
        cur_chr = seats[i]
        if cur_chr == '1':
            cur_flag = i
        else:
            cur_flag = -1
        
        if cur_flag != -1:
            if last_flag != -1:
                sub = cur_flag - last_flag
                min_num = min(min_num, sub)
            last_flag = cur_flag

    return min_num

max_dist = 0
for i in range(N):
    for j in range(i + 1, N):
        if seats[i] == '1' or seats[j] == '1':
            continue

        seats[i], seats[j] = '1', '1'
        max_dist = max(max_dist, get_dist())
        seats[i], seats[j] = '0', '0'

print(max_dist)
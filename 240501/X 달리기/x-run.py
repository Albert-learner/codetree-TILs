X = int(input())

cur_pos, cur_speed = 0, 1
total_times = 0

while True:
    cur_pos += cur_speed
    total_times += 1
    cur_speed += 1
    gradients = 0

    if cur_pos == X:
        break

    for i in range(cur_speed):
        gradients += i
    
    if X - (cur_pos + cur_speed) < gradients:
        cur_speed -= 1

    stays = 0
    for i in range(cur_speed):
        stays += i
    if X - (cur_pos + cur_speed) < stays:
        cur_speed -= 1

print(total_times)
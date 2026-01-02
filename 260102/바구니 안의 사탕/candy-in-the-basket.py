# 변수 선언 및 입력:
n, k = tuple(map(int, input().split()))
candies = [(-1, -1)]
for _ in range(n):
    cnt, x = tuple(map(int, input().split()))
    # 추후에 x순으로 오름차순 정렬이 되도록
    # x값을 첫 번째 값으로 하여 넣어줍니다.
    candies.append((x, cnt))


# 해당 내용물의 위치를 반환합니다.
def get_pos_of_candy(candy_idx):
    x, _ = candies[candy_idx]
    return x


# 해당 내용물에 들어 있는 사탕 수를 반환합니다.
def get_num_of_candy(candy_idx):
    _, cnt = candies[candy_idx]
    return cnt


# x순으로 오름차순 정렬해줍니다.
candies.sort()

# 가능한 구간 중 최대 사탕의 수를 구합니다.
ans = 0

# 구간을 잡아봅니다.
# 구간 내에 있는 사탕의 수를 계속 계산하여 관리해줍니다.
total_nums = 0
j = 0
for i in range(1, n + 1):
    # 구간의 크기가 2K보다 같거나 작은 경우에 한하여 최대로 진행합니다.
    while j + 1 <= n and get_pos_of_candy(j + 1) - get_pos_of_candy(i) <= 2 * k:
        total_nums += get_num_of_candy(j + 1)
        j += 1
    
    # 현재 구간 [i, j]는 
    # i를 시작점으로 하는
    # 가장 긴 구간이므로
    # 구간 내 최대 사탕의 수를 갱신해줍니다.
    ans = max(ans, total_nums)

    # 다음 구간으로 넘어가기 전에
    # i번째에 해당하는 사탕을 구간에서 제외시킵니다.
    total_nums -= get_num_of_candy(i)

print(ans)

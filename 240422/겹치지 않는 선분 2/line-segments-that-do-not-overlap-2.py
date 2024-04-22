N = int(input())
lines = [list(map(int, input().split())) for _ in range(N)]

def check_cross(num):
    some = 0

    p0 = lines[num][0]
    p1 = lines[num][1]
    p_diff = p1 - p0

    for p in range(N):
        if p == num:
            continue

        cp0, cp1 = lines[p][0], lines[p][1]
        cp_diff = cp1 - cp0

        up = p0 * cp_diff - cp0 * p_diff
        down = cp_diff - p_diff

        if down != 0:
            result = up / down

            if min(p0, p1) <= result <= max(p0, p1) and min(cp0, cp1) <= result <= max(cp0, cp1):
                some += 1
    
    if some == 0:
        return True
    else:
        return False

cnts = 0
for i in range(N):
    if check_cross(i):
        cnts += 1

print(cnts)

# # 모범답안
# # 변수 선언 및 입력
# n = int(input())
# x = [
#     tuple(map(int, input().split()))
#     for _ in range(n)
# ]

# ans = 0


# # 다른 선분과 겹치지 않는 선분의 수를 구합니다.
# for i in range(n):
# 	# i번째 선분이 다른 선분과 겹치지 않는지 확인합니다.
# 	overlap = False
	
# 	for j in range(n):
# 		# 자기 자신은 제외합니다.
# 		if j == i:
# 			continue
		
# 		# x1이 큰 쪽이 x2가 더 작다면 겹치게 됩니다.
# 		if (x[i][0] <= x[j][0] and x[i][1] >= x[j][1]) or (x[i][0] >= x[j][0] and x[i][1] <= x[j][1]):
# 			overlap = True
# 			break
	
#     # 겹치지 않았다면 정답의 개수에 하나를 추가합니다.
# 	if overlap == False:
# 		ans += 1

# print(ans)
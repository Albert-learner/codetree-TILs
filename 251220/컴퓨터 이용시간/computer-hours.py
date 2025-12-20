import heapq

# 변수 선언 및 입력:
n = int(input())

# 각 사람의 컴퓨터 이용시간을 선분이라 생각합니다.
segments = [
    tuple(map(int, input().split()))
    for _ in range(n)
]
# 각 사람별로 할당된 컴퓨터 번호를 관리합니다.
assigned_nums = [0] * n

# 쉬고 있는 n개의 컴퓨터 번호를 
# priority queue에 넣어줍니다.
computers = []
for i in range(1, n + 1):
    heapq.heappush(computers, i)

# 각 선분을 두 지점으로 나눠 담은 뒤,
# 정렬해줍니다.
# 이때 (x좌표, +1-1값, 선분 번호)
# 형태로 넣어줍니다.
# +1은 시작점
# -1은 끝점을 뜻합니다.
points = []
for i, (x1, x2) in enumerate(segments):
    points.append((x1, +1, i)) # 시작점
    points.append((x2, -1, i)) # 끝점

# 정렬을 진행합니다.
points.sort()

for x, v, index in points:
    # 시작점인 경우입니다.
    if v == +1:
        # 아직 남아있는 컴퓨터 중
        # 번호가 가장 작은 컴퓨터를 선택합니다.
        # 선택된 컴퓨터는 목록에서 제거해줍니다.
        computer_num = heapq.heappop(computers)

        # 해당 사용자에게 컴퓨터 번호를 매칭해줍니다.
        assigned_nums[index] = computer_num

    # 끝점인 경우입니다.
    else:
        # 해당 사람의 컴퓨터를 다시
        # 사용가능 상태로 만들어줍니다.
        computer_num = assigned_nums[index]
        heapq.heappush(computers, computer_num)

# 각 사람이 사용한 컴퓨터 번호를 출력합니다.
for num in assigned_nums:
    print(num, end=" ")

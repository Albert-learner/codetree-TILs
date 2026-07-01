# 변수 선언 및 입력:
q = int(input())

# 집합 S의 현재 상황을 하나의 정수 값으로 나타내어 관리합니다.
# S에 존재하는 수가 x1, x2, ..., xk라 한다면
# snum = 2^x1 + 2^x2 + .. 2^xk가 되도록 합니다.
snum = 0

for _ in range(q):
    command = input()

    if command.startswith("add"):
        _, x = tuple(command.split())
        x = int(x)
        
        # 집합 S에 x를 추가합니다.
        # 이미 x가 집합 S에 들어가 있지 않은 경우에만 넣어줍니다.
        if ((snum >> x) & 1) == 0:
            snum ^= (1 << x)

    elif command.startswith("delete"):
        _, x = tuple(command.split())
        x = int(x)

        # 집합 S에 x를 제거힙니다.
        # 이미 x가 집합 S에 들어가 있는 경우에만 제거합니다.
        if ((snum >> x) & 1) == 1:
            snum ^= (1 << x)
        
    elif command.startswith("print"):
        _, x = tuple(command.split())
        x = int(x)

        # 집합 S에 x가 있는지 확인합니다.
        print(((snum >> x) & 1))
    
    elif command.startswith("toggle"):
        _, x = tuple(command.split())
        x = int(x)

        # 집합 S에 x를 toggle해줍니다.
        snum ^= (1 << x)

    else:
        # 집합 S를 공집합으로 만들어줍니다.
        snum = 0

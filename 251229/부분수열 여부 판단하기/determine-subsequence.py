# 변수 선언 및 입력:
n, m = tuple(map(int, input().split()))
A = [0] + list(map(int, input().split()))
B = [0] + list(map(int, input().split()))


def is_subsequence():
    i = 1
    # B의 원소를 기준으로
    # 순서대로 매칭이 가능한지를 확인합니다.
    for j in range(1, m + 1):
        # A의 원소가 B의 j번째 원소와
        # 일치해지는 위치를 구해줍니다.
        while i <= n and A[i] != B[j]:
            i += 1
        
        # 만약 수열 A에서 일치하는 원소를 찾지 못햇다면
        # 부분수열이 아닙니다.
        if i == n + 1:
            return False
        # 일치한다면
        # A 원소의 위치도 한칸 앞으로 이동시켜 줍니다.
        else:
            i += 1

    # 전부 매칭하는게 가능했다면
    # 부분수열입니다.
    return True


# 부분수열이라면 Yes를 출력합니다.
if is_subsequence():
    print("Yes")
else:
    print("No")

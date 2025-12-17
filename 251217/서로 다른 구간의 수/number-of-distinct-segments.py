# 변수 선언 및 입력:
n = int(input())
segments = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

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

# 각 점을 순서대로 순회합니다.
# 등장하고 아직 사라지지 않은
# 선분을 hashset으로 관리합니다.
segs = set()

ans = 0 # 서로 다른 구간의 수를 저장합니다.
for x, v, index in points:
    # 시작점인 경우입니다.
    if v == +1:
        # 남아있는 선분이 없다면
        # 답을 갱신합니다.
        if not segs:
            ans += 1
        
        # 해당 선분 번호를 hashset에 넣어줍니다.
        segs.add(index)

    # 끝점인 경우입니다.
    else:
        # 해당 선분을 제거합니다.
        segs.remove(index)

print(ans)

# 변수 선언 및 입력:
n, m = tuple(map(int, input().split()))
jewels = [
    tuple(map(int, input().split()))
    for _ in range(n)
]
ans = 0

# 가치 / 무게가 내림차순이 되도록 정렬합니다.
jewels.sort(key=lambda x: -x[1] / x[0])

for w, v in jewels:
    # 현재 보석을 온전히 다 담을 수 있다면 그대로 담아줍니다.
    if m >= w:
        m -= w
        ans += v
    # 만약 부분만 담을 수 있다면
    # 비율에 맞춰 담아준 뒤 종료합니다.
    else:
        ans += m / w * v
        break

print(f"{ans:.3f}")

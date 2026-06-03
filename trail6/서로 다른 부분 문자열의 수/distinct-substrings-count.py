# 변수 선언 및 입력:
s = input()

# 2개의 polynomial rolling 해싱을 위한 p, m 값을 정의합니다.
p = [31, 37]
m = [int(1e9) + 7, int(1e9) + 9]

n = len(s)

# p^i, 값을 m으로 나눈 나머지를 관리합니다.
p_pow = [
    [0] * (n + 1)
    for _ in range(2)
]


# 소문자 알파벳을 수로 변경합니다.
def to_int(c):
    return ord(c) - ord('a') + 1


# p_pow 값을 계산합니다.
for k in range(2):
    # p_pow[i] = p^i % m
    p_pow[k][0] = 1
    for i in range(1, n + 1):
        p_pow[k][i] = (p_pow[k][i - 1] * p[k]) % m[k]

# 동일한 길이 l에 대해
# 문자열의 hashing값을 set으로 관리하여
# 서로 다른 문자열의 수를 누적해줍니다.
ans = 0
for l in range(1, n + 1):
    hs = set()

    # s에서 구간 [0, l - 1]에 해당하는 해싱값을 계산합니다.
    h = [0, 0]
    for k in range(2):
        for i in range(l):
            h[k] = (h[k] + to_int(s[i]) * p_pow[k][l - 1 - i]) % m[k]

    # set에 넣어줍니다.
    hs.add((h[0], h[1]))

    # [i, i + l - 1] 구간을 부분문자열로 하는 경우를 전부 탐색합니다.
    for i in range(1, n - l + 1):
        for k in range(2):
            # hash 값을 갱신해줍니다.
            h[k] = (h[k] * p[k] - to_int(s[i - 1]) * p_pow[k][l] + to_int(s[i + l - 1])) % m[k]
            # 값을 양수로 변환해줍니다.
            if h[k] < 0:
                h[k] += m[k]
        
        # set에 넣어줍니다.
        hs.add((h[0], h[1]))

    # 길이가 l인 문자열 중 서로 다른 문자열의 수를 더해줍니다.
    ans += len(hs)

print(ans)

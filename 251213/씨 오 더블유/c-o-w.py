# 변수 선언 및 입력:
n = int(input())
word = input()
L, R = [0] * n, [0] * n
ans = 0

# L 배열을 채워줍니다.
# L[i] = 0번부터 i번 문자 C의 개수
L[0] = 1 if word[0] == 'C' else 0
for i in range(1, n):
    L[i] = L[i - 1] + (1 if word[i] == 'C' else 0)

# R 배열을 채워줍니다.
# R[i] = i번부터 n - 1번 문자 중 W의 개수
R[n - 1] = 1 if word[n - 1] == 'W' else 0
for i in range(n - 2, -1, -1):
    R[i] = R[i + 1] + (1 if word[i] == 'W' else 0)

# 각 위치 i에 대해
# word[i]가 O라면
# i보다 왼쪽에 있는 C의 개수인 L[i - 1]과
# i보다 오른쪽에 있는 W의 개수인 R[i + 1]의 곱이
# i를 중심으로 하여 COW 조합을 만들어 내는 숫자가 됩니다.
for i in range(1, n - 1):
    if word[i] == 'O':
        ans += L[i - 1] * R[i + 1]

print(ans)

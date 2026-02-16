# 변수 선언 및 입력:
n = int(input())
a = input()
b = input()

# 이 문제는 앞서 나온 'G & H 반전시키기' 문제와 매우 비슷하며,
# 구간을 겹치지 않을 때 가장 적은 길이로 반전을 할 수 있습니다.

# 계속 매치가 되다가 
# 처음으로 미스매치가 되는 순간을 잡아
# 그 횟수를 계산합니다.
# 그 후 최대 4자리까지만 확인한 후 다시 미스매치가 되는 순간을 찾습니다.
ans = 0
mismatched = False
cnt = 0
for i in range(n):
    if a[i] != b[i]:
        # 다시 미스매치가 처음으로 발생하는 순간이라면
        # 답을 갱신해줍니다.
        if not mismatched or cnt >= 4:
            mismatched = True
            ans += 1
            cnt = 1
        else:
            cnt += 1
       
    else:
        mismatched = False
        cnt = 0

print(ans)

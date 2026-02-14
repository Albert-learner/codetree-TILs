# 변수 선언 및 입력:
n = int(input())
a = input()
b = input()

# 계속 매치가 되다가 
# 처음으로 미스매치가 되는 순간을 잡아
# 그 횟수를 계산합니다. 
ans = 0
mismatched = False
for i in range(n):
    if a[i] != b[i]:
        # 다시 미스매치가 처음으로 발생하는 순간이라면
        # 답을 갱신해줍니다.
        if not mismatched:
            mismatched = True
            ans += 1
       
    else:
        mismatched = False

print(ans)

from sys import stdin
n, m = list(map(int, stdin.readline().split())) #크기와 금 가격
arr_2d = [list(map(int, stdin.readline().split())) for _ in range(n)]
#n*n이 될때까지 채굴, 대각선 길이가 n//2이고 k-1임, 인덱스가 k번의미!
#중앙에서 전체 범위 캐는 것이 최대치임 범위가 더 커져서 사이드에서 최대치 채굴하더라고 금의 갯수는 변동없음
price = [k*k + (k+1)*(k+1) for k in range(n//2*2+1)]
# print(price)

def in_range(x, y):
    return 0<=x<n and 0<=y<n

#넓은 범위에서 이익 남는지를 먼저 봄, 바로 정지!, 전 범위보다 더 많이 캘 수는 없다.
def check(x, y, size):
    dxs, dys = [0,1,0,-1], [1,0,-1,0] #우-하-좌-상 1,3이 아래,위
    # dxs2, dys2 = [1,1], [-1,1] #내려가는 대각선 봄
    # dxs3, dys3 = [-1,-1], [-1,1] #올라가는 대각선 봄
    
    total = arr_2d[x][y]
    for k in range(1,size+1):
        for d in range(4):
            nx, ny = x+dxs[d]*k,y+dys[d]*k
            if in_range(nx, ny):
                total += arr_2d[nx][ny]
            if d % 2 != 0: #상,하의 경우 대각선 이동
                for s in range(1,k):
                    for dy in [-1, 1]:
                        sx, sy = nx+(d-2)*s, ny+dy*s
                        if in_range(sx, sy):
                            total += arr_2d[sx][sy]
    return total

base=0
for i in range(n):
    for j in range(n):
        for k in range(len(price)-1,-1,-1):
            num = check(i, j, k)
            # print(i,j,k,num, num*m, price[k])
            if num*m >= price[k]:
                base = max(base, num)
                break
print(base)
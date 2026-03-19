# 변수 선언 및 입력:
n, m = tuple(map(int, input().split()))

edge = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

ans = 0
vcnt = 0
ecnt = 0

# n - 1개의 간선 정보를 입력받습니다.
for _ in range(m):
    x, y = tuple(map(int, input().split()))
    edge[x].append(y)
    edge[y].append(x)


# dfs 탐색을 진행합니다.
def dfs(x):
    global vcnt, ecnt
    
    for y in edge[x]:
        # 간선 개수를 세어줍니다.
        ecnt += 1

        # 이미 방문한 정점이면 스킵합니다.
        if visited[y]: 
            continue

        visited[y] = True
        vcnt += 1 # 정점 개수를 세어줍니다.
        dfs(y)


# 모든 정점을 방문해 트리 여부를 탐색합니다.
for i in range(1, n + 1):
    if visited[i]: 
        continue
    
    visited[i] = True
    vcnt = 1
    ecnt = 0
    dfs(i)

    # 2번씩 중복 세어진 경우를 처리합니다.
    ecnt = ecnt // 2
    
    # 트리의 성질을 만족한다면
    # 답을 갱신해줍니다.
    if vcnt - 1 == ecnt:
        ans += 1

# 컴퍼넌트 중 트리인 것의 개수를 출력합니다.
print(ans)

import sys
sys.setrecursionlimit(10000)

# 변수 선언 및 입력:
n = int(input())

# 트리를 전위순회한 결과를 입력받습니다.
pre_order = [0] * (n + 1)
for i in range(1, n + 1):
    pre_order[i] = int(input())

post_order = [0] * (n + 1)
cnt = 1


# 트리의 전위 순회 결과를 바탕으로 해당 서브트리에서
# 루트, 왼쪽 서브트리, 오른쪽 서브트리를 잘 관리하여 DFS합니다.
# 전위 순회의 [l, r] 정보를 이용한 탐색을 진행합니다.
def dfs(l, r):
    global cnt

    # 탐색이 불가능한 종료조건에 해당합니다.
    if l > r: 
        return

    # l = r이 되면
    # 전위, 중위, 후위 순회 결과가 전부 단일 노드로서 동일해집니다.
    if l == r:
        post_order[cnt] = pre_order[l]
        cnt += 1
        return

    # 전위 순회이므로
    # pre_order[l]은 루트 노드임이 자명합니다.
    # 전위 순회는 루트, 왼쪽 서브트리, 오른쪽 서브트리 순이고
    # 이진 검색 트리를 기반으로 하고 있기에 
    # 오른쪽 서브트리의 모든 노드는 루트 노드 값보다 커야하므로
    # 최초로 루트 노드보다 값이 큰 index를 찾습니다.
    right_subtree_st = r + 1
    for i in range(l + 1, r + 1):
        if pre_order[l] < pre_order[i]:
            right_subtree_st = i
            break

    # 전위 순회의 왼쪽 서브 트리 정보를 이용하여 재귀적으로 탐색합니다.
    dfs(l + 1, right_subtree_st - 1)

    # 전위 순회의 오른쪽 서브 트리 정보를 이용하여 재귀적으로 탐색합니다.
    dfs(right_subtree_st, r)

    # 후위 순회의 경우 (왼쪽 서브 트리, 오른쪽 서브 트리, 현재 노드)
    # 순으로 순서가 구성되어야 하므로
    # 위의 두 재귀 함수 (왼쪽, 오른쪽) 탐색을 끝내고 난 이후에
    # 현재 노드의 위치 값을 적어줍니다.
    post_order[cnt] = pre_order[l]
    cnt += 1

   
# 트리의 전위 순회 결과를 바탕으로 해당 서브트리에서
# 루트, 왼쪽 서브트리, 오른쪽 서브트리를 잘 관리하여 DFS합니다.
dfs(1, n)

# 후위순회의 번호를 순서대로 출력합니다.
for i in range(1, n + 1):
    print(post_order[i])

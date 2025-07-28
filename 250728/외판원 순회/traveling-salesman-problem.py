n = int(input())
A = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
def solve_min_hamiltonian_cost(n, cost):
    visited = [False] * n
    x_pos = []
    y_pos = []
    ans = [float('inf')]

    def calc_min_sum(curX):
        total = 0
        for i in range(n - 1):
            total += cost[x_pos[i]][y_pos[i]]
        if cost[curX][0] == 0:
            return
        total += cost[curX][0]
        ans[0] = min(ans[0], total)

    def find_min(cnt, curX):
        if cnt == n - 1:
            calc_min_sum(curX)
            return
        for i in range(n):
            if visited[i] or cost[curX][i] == 0:
                continue
            visited[curX] = True
            x_pos.append(curX)
            y_pos.append(i)
            find_min(cnt + 1, i)
            x_pos.pop()
            y_pos.pop()
            visited[curX] = False

    find_min(0, 0)
    return ans[0]

print(solve_min_hamiltonian_cost(n, A))
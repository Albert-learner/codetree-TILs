n, m, k = map(int, input().split())
command = list(map(int, input().split()))


#command 순서가 올 때 마다 , 어느 말을 이동시킬 것인지, 결정해야한다.
horse_status = [1 for _ in range(k)]
MAX = -1

def calc():
    global horse_status
    score = 0
    for piece in horse_status:
        score += (piece >= m)
    return score

def backtracking(curr_idx):
    global n, m, k, command, horse_status, MAX

    MAX = max(MAX, sum(1 for val in horse_status if val >= m))
    # MAX = max(MAX, calc()) #해설코드

    if curr_idx == n:
        return
    for i in range(k): #0부터 k-1 까지의 말을 선택.

        if horse_status[i] >= m:
            continue

        temp = horse_status[i]
        horse_status[i] += command[curr_idx]
        backtracking(curr_idx + 1)
        horse_status[i] -= command[curr_idx]

backtracking(0)
print(MAX)
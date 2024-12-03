K, N = map(int, input().split())

answer = []

def print_answer():
    for elem in answer:
        print(elem, end = " ")
    print()

def choose_num(curr_num):
    if curr_num == N + 1:
        print_answer()
        return

    for i in range(1, K + 1):
        answer.append(i)
        choose_num(curr_num + 1)
        answer.pop()

    return

choose_num(1)
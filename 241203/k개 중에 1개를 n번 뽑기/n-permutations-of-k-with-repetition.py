K, N = map(int, input().split())

answer = []

def print_answer():
    for elem in answer:
        print(elem, end = " ")
    print()

def choose(cur_num):
    if cur_num == K + 1:
        print_answer()
        return
    
    for i in range(1, N + 1):
        answer.append(i)
        choose(cur_num + 1)
        answer.pop()
    return

choose(1)
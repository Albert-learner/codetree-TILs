N, Q = map(int, input().split())
n_lst = list(map(int, input().split()))

questions = []
for _ in range(Q):
    question = list(map(int, input().split()))
    if len(question) == 2:
        question[1] = int(question[1])
    else:
        question[1], question[2] = int(question[1]) - 1, int(question[2]) - 1
    questions.append(question)

for question in questions:
    if question[0] == 1:
        print(n_lst[question[1] - 1])
    elif question[0] == 2:
        first_idx = 0
        for idx, n in enumerate(n_lst):
            if n == question[1]:
                first_idx = idx + 1
                break
        print(first_idx)
    else:
        for i in range(question[1], question[2] + 1):
            print(n_lst[i], end = ' ')
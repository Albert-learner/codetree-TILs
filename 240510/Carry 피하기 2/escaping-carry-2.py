from collections import deque

N = int(input())
numbers = [int(input()) for _ in range(N)]
numbers_dq = deque([deque(map(int, list(str(number)))) for number in numbers])

max_len = len(str(max(numbers)))
for n_idx, number_dq in enumerate(numbers_dq):
    if len(number_dq) < max_len:
        diff = max_len - len(number_dq)
        for _ in range(diff):
            number_dq.appendleft(0)

numbers_lst = []
for number_dq in numbers_dq:
    number_lst = list(number_dq)
    numbers_lst.append(number_lst)

answer = -1
carry = False
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            first, second, third = numbers_lst[i], numbers_lst[j], numbers_lst[k]
            for f, s, t in zip(first, second, third):
                if f + s + t >= 10:
                    carry = True
                    break

            if carry:
                carry = False
                continue
            else:
                num_str1 = "".join(map(str, first))
                num_str2 = "".join(map(str, second))
                num_str3 = "".join(map(str, third))
                answer = max(answer, int(num_str1) + int(num_str2) + int(num_str3))

print(answer)
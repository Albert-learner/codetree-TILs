A, B, x, y = map(int, input().split())

if A > B:
    A, B = B, A

if x > y:
    x, y = y, x

cases = []
if A == x and B == y:
    cases.append(0)

line = [0] * 101
first_case, second_case, third_case = 0, 0, 0
line[A], line[B] = 1, 2
first_case = abs(B - A)
cases.append(first_case)

second_case = abs(A - x) + abs(B - y)
cases.append(second_case)


third_case = abs(A - y) + abs(B - x)
cases.append(third_case)

print(min(cases))
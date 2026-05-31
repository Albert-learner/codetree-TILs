n, c = input().split()
n = int(n)
S = input()

# Please write your code here.
input_strs_lst = sorted(S.split(c), key = lambda x: len(x), reverse = True)
answer = -1

for input_str in input_strs_lst:
    m_inp_str = '#' + '#'.join(input_str) + '#'

    n = len(m_inp_str)
    A = [0] * n
    r, p = -1, -1

    for i in range(n):
        if r < i:
            A[i] = 0
        else:
            ii = 2 * p - i
            A[i] = min(r - i, A[ii])

        while i - A[i] - 1 >= 0 and i + A[i] + 1 < n and m_inp_str[i - A[i] - 1] == m_inp_str[i + A[i] + 1]:
            A[i] += 1

        if i + A[i] > r:
            r, p = i + A[i], i

    ans = 0
    for i in range(n):
        ans = max(ans, 2 * A[i] + 1)

    answer = max(answer, ans // 2)

print(answer)
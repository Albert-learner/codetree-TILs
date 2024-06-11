N, M = map(int, input().split())
n_lst = list(map(int, input().split()))

m_cnts= 0
for n in n_lst:
    if n == M:
        m_cnts += 1

print(m_cnts)
N, M = map(int, input().split())
a_seq = list(map(int, input().split()))
m_pairs = [list(map(int, input().split())) for _ in range(M)]

for start, end in m_pairs:
    print(sum(a_seq[start - 1:end]))
N, M = map(int, input().split())
a_seq = list(map(int, input().split()))

def operate(m, a_seq):
    answer = 0
    while m >= 1:
        if m % 2 == 1:
            answer += a_seq[m - 1] 
            m -= 1
        else:
            answer += a_seq[m - 1]
            m //= 2
    
    return answer

print(operate(M, a_seq))
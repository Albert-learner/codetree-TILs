N = int(input())
seq = list(map(int, input().split()))

# # 남의 코드 참고하여 푼 풀이
# def find_max(n):
#     if n == len(seq):
#         return seq[n - 1]

#     return max(seq[n], find_max(n + 1))

# print(find_max(0))

def find_max(n):
    if n == 0:
        return seq[n]

    return max(seq[n], find_max(n - 1))

print(find_max(N - 1))
N = int(input())

def recur_eval_sum(n):
    if n == 1:
        return 0

    if n % 2 == 0:
        return recur_eval_sum(n // 2) + 1
    else:
        return recur_eval_sum(n // 3) + 1

print(recur_eval_sum(N))
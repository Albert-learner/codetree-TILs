N = int(input())

answer = ''
for n in range(2, N):
    if N % n == 0:
        answer += 'C'
        break

if answer != 'C':
    answer = 'N'

print(answer)
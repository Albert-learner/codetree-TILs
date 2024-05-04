N = int(input())
n_lst = list(map(int, input().split()))

odds, evens = 0, 0
for n in n_lst:
    if n % 2 != 0:
        odds += 1
    else:
        evens += 1

answer = 0
if evens > odds:
    answer = odds * 2 + 1
elif evens == odds:
    answer = evens + odds
else:
    answer = evens * 2 
    diff = odds - evens

    if diff % 3 == 0:
        answer += (diff // 3) * 2
    else:
        if (diff % 3) % 2 == 0:
            answer = diff // 3 * 2 + 1
        else:
            answer += diff // 3 * 2 - 1

print(answer)
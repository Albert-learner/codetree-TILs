N, Q = map(int, input().split())
arr = [int(input()) for _ in range(N)]
queries = [tuple(map(int, input().split())) for _ in range(Q)]

# Please write your code here.
pref1 = [0] * (N + 1)
pref2 = [0] * (N + 1)
pref3 = [0] * (N + 1)

for i in range(1, N + 1):
    g = arr[i - 1] 
    pref1[i] = pref1[i - 1]
    pref2[i] = pref2[i - 1]
    pref3[i] = pref3[i - 1]

    if g == 1:
        pref1[i] += 1
    elif g == 2:
        pref2[i] += 1
    elif g == 3:
        pref3[i] += 1

out_lines = []
for a, b in queries:
    cnt1 = pref1[b] - pref1[a - 1]
    cnt2 = pref2[b] - pref2[a - 1]
    cnt3 = pref3[b] - pref3[a - 1]
    out_lines.append(f"{cnt1} {cnt2} {cnt3}")

print("\n".join(out_lines))
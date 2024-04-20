developers = list(map(int, input().split()))
developers.sort()

if developers[0] + developers[2] == developers[1] + developers[3] or developers[1] + developers[3] == developers[4] or developers[4] == developers[0] + developers[2]:
    print(-1)
else:
    max_team = max(developers[0] + developers[2], developers[1] + developers[3], developers[4])
    min_team = min(developers[0] + developers[2], developers[1] + developers[3], developers[4])

    print(max_team - min_team)
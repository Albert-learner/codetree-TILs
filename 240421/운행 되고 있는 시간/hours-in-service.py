N = int(input())
developers = [list(map(int, input().split())) for _ in range(N)]

run_times = []
for i in range(N):
    fired = developers[i]
    run_time = []
    for j in range(N):
        if developers[j] != fired:
            start, end = developers[j]
            run_time.extend(list(range(start, end)))
        else:
            continue
    run_times.append(list(set(sorted(run_time))))

max_run_time = max([len(run_time) for run_time in run_times])
print(max_run_time)
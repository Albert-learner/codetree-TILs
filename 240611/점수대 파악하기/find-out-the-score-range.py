scores = list(map(int, input().split()))

n_scores = []
for score in scores:
    if score == 0:
        break
    else:
        n_scores.append((score // 10) * 10)

scores_cntr = {score: 0 for score in range(10, 101, 10)}
for n_score in n_scores:
    if n_score in scores_cntr:
        scores_cntr[n_score] += 1

scores_sort = sorted([(n_score, cnts) for n_score, cnts in scores_cntr.items()], key = lambda x: x[0], reverse = True)
for n_score, cnts in scores_sort:
    print(f"{n_score} - {cnts}")
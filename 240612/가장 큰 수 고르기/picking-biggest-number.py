n_lst = list(map(int, input().split()))

# print(max(n_lst))

max_val = arr[0]
	
# 10개의 숫자들 중 최댓값을 구합니다.
for elem in arr:
	if elem > max_val:
		max_val = elem
	
# 최댓값을 출력합니다.
print(max_val)
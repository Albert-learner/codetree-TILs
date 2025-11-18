t = int(input())
for _ in range(t):
    m = int(input())
    arr = list(map(int, input().split()))

    # Please write your code here.
    queue = []
    for idx, elem in enumerate(arr, 1):
        if idx % 2 == 1:
            queue.append(elem)
            print(queue[len(queue) // 2], end=' ')
        else:
            queue.append(elem)

    queue.sort()
    print()
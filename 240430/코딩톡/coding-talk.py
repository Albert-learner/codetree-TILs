N, M, P = map(int, input().split())
messages = []
not_reads = []
for _ in range(M):
    c, u = input().split()
    messages.append(c)
    not_reads.append(int(u))

read_chk = [False] * 26
for i in range(M):
    if not_reads[P - 1] == 0:
        break

    if i >= P - 1:
        message = ord(messages[i]) - ord('A')
        read_chk[message] = True
    elif not_reads[i] == not_reads[P - 1]:
        message = ord(messages[i]) - ord('A')
        read_chk[message] = True


if not_reads[P - 1] == 0:
    print()
else:
    for i in range(N):
        if not read_chk[i]:
            print(chr(i + ord('A')), end = ' ')


# # 모범답안
# import sys

# n, m, p = tuple(map(int, input().split()))
# message = [
#     list(input().split())
#     for _ in range(m)
# ]

# # 모두 읽은 채팅이라면 읽지 않은 사람은 없습니다.
# if int(message[p - 1][1]) == 0:
#     sys.exit()

# # 각 사람에 대해 채팅을 읽었을지 안 읽었을지 판단합니다.
# for i in range(n):
#     # read : 확실하게 채팅을 읽었으면 true
#     person = chr(ord('A') + i)
#     read = False

#     # 만약 p번 메시지를 읽은 사람 수와 같은 채팅을 기준으로
#     # 한번이라도 채팅을 쳤다면 확실하게 채팅을 읽었습니다.
#     for c, u in message:
#         u = int(u)
#         if u >= int(message[p - 1][1]) and c == person:
#             read = True
    
#     if read == False:
#         print(person, end=" ")
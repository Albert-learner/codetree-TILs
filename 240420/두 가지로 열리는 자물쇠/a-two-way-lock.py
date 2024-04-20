N = int(input())
a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())

a1_lst = [i if 1 <= i <= N else i - N if i > N else i + N for i in range(a1 - 2, a1 + 3)]
b1_lst = [i if 1 <= i <= N else i - N if i > N else i + N for i in range(b1 - 2, b1 + 3)]
c1_lst = [i if 1 <= i <= N else i - N if i > N else i + N for i in range(c1 - 2, c1 + 3)]

a2_lst = [i if 1 <= i <= N else i - N if i > N else i + N for i in range(a2 - 2, a2 + 3)]
b2_lst = [i if 1 <= i <= N else i - N if i > N else i + N for i in range(b2 - 2, b2 + 3)]
c2_lst = [i if 1 <= i <= N else i - N if i > N else i + N for i in range(c2 - 2, c2 + 3)]

first_comb = set()
for a_one in a1_lst:
    for b_one in b1_lst:
        for c_one in c1_lst:
            first_comb.add((a_one, b_one, c_one))
first_comb = sorted(first_comb)

second_comb = set()
for a_two in a2_lst:
    for b_two in b2_lst:
        for c_two in c2_lst:
            second_comb.add((a_two, b_two, c_two))
second_comb = sorted(second_comb)

print(len(set(first_comb + second_comb)))
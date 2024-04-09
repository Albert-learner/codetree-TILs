class Members:
    def __init__(self, name, score):
        self.name = name
        self.score = score

members = []
for _ in range(5):
    name, score = input().split()
    score = int(score)
    members.append(Members(name, score))

min_member = min(members, key = lambda x: x.score)
print(min_member.name, min_member.score)
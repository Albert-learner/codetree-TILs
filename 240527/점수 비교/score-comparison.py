a_math, a_english = map(int, input().split())
b_math, b_english = map(int, input().split())

print(1 if a_math > b_math and a_english > b_english else 0)
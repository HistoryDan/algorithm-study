import sys

scores = []
for _ in range(5):
    score = int(sys.stdin.readline())
    if score < 40:
        score = 40
    scores.append(score)

avg = sum(scores) // 5
print(avg)
import sys 
scores = []

for i in range(1,9):
    score = int(sys.stdin.readline().rstrip())
    scores.append(score)

ref = scores.copy()
scores = sorted(scores, reverse = True)
scores = scores[:5]
indices = []

for score in scores:
    indices.append(ref.index(score)+1)

indices.sort()
print(sum(scores))
print(*indices)

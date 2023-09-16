import sys
n = sys.stdin.readline().rstrip()
scores = [int(score) for score in sys.stdin.readline().rstrip().split()]

avg = 0 
best = max(scores)
scores_n = [score / best * 100 for score in scores]

for s in scores_n:
  avg += s
avg /= int(n)

print(avg)


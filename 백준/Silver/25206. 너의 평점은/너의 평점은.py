import sys
credits = []
scores = []
table = {'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0, 'C+':2.5,
        'C0':2.0, 'D+':1.5, 'D0':1.0, 'F':0}
result = 0

for i in range(20):
  line = sys.stdin.readline().rstrip().split()
  if line[2] == 'P':
    continue
  else:
    credits.append(float(line[1]))
    scores.append(line[2])

for i in range(len(credits)):
  for t in table:
    if scores[i] == t:
      result += (table[t] * credits[i])

result /= sum(credits)

print(result)
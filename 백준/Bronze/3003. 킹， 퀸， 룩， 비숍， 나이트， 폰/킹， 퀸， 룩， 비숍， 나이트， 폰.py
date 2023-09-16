pieces = [int(i) for i in input().split()]
answers = [1,1,2,2,2,8]

for i in range(6):
  answers[i] = answers[i] - pieces[i]

print(*answers)
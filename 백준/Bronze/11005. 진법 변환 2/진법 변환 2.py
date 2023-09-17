given = input().split()
number = int(given[0])
system = int(given[1])
result = []
answer = []

while number != 0:
  rest = number % system
  result.append(rest)
  number = number // system

for i in range(len(result)-1,-1,-1):
  if result[i] > 9:
    result[i] = chr(result[i] - 10 + ord('A'))
  answer.append(result[i])

print(''.join([str(a) for a in answer]))
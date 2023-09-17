given = input().split()
number = given[0]
system = int(given[1])
digits = ['0','1','2','3','4','5','6','7','8','9']
result = 0

for i in range(len(number)):
  if number[i] in digits:
    result += int(number[i]) * (system ** (len(number) -i-1))
  else:
    result += (ord(number[i]) - 55) * (system ** (len(number) -i-1))

print(result)
  
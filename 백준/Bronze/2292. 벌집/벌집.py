num = int(input())
answer = 1
temp = 1
i = 0

while True:
  temp += (6*i)
  if temp >= num:
    answer = 1 + i
    break
  i += 1

print(answer)

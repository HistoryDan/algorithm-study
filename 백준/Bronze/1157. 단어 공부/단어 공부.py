word = input().upper()
count = 0
question = False

for i in range(65, 91):
  temp = word.count(chr(i))
  if temp > count:
    count = temp
    best = chr(i)
    question = False
  elif temp == count:
    question = True
    
if question:
  print('?')
else:
  print(best)
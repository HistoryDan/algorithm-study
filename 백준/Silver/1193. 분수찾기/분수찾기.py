idx = int(input())
upper = 1
i = 0

while True:
  if (idx <= upper) and (idx >= upper - (1+4*i)//2):
    row = 1 + (upper - idx)
    col = 1 + (2*i) - (upper - idx)
    break
  elif (idx >= upper - (4*i)) and (idx < upper - (1+4*i)//2):
    row = ((1+4*i) // 2) - ((upper - (1+4*i)//2 - 1) - idx)
    col = 1 + ((upper - (1+4*i)//2 - 1) - idx)
    break
  i += 1
  upper += (1 + 4*i)

print(str(row)+'/'+str(col))
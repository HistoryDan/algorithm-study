rep = int(input())

for _ in range(rep):
  h,w,n = map(int, input().split())
  x = n % h
  if x == 0:
    x = h
  y = 0
  
  while n > 0:
    n -= h
    y += 1

  if y < 10:
    y = '0' + str(y)
  
  print(str(x) + str(y))
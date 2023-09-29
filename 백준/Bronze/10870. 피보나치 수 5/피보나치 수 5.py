import sys

n = int(sys.stdin.readline().rstrip())
a1 = 0
a2 = 1

if n == 0 :
  print(0)

elif n == 1:
  print(1)
  
else:
  for _ in range(n-1):
    total = a1 + a2
    a1 = a2
    a2 = total

  print(total)
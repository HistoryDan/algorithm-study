import sys

n = int(sys.stdin.readline().rstrip())
for i in range(1, 2*n):
  if i <= n:
    print('*'*i + ' '*(2*n-2*i) + '*'*i)
  else:
    print('*'*(2*n - i) + ' '*(2*(i - n))+ '*'*(2*n - i)) 
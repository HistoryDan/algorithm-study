import sys

total = int(input())
types = int(input())
check = 0

for i in range(types):
    a, b = map(int, sys.stdin.readline().split())
    check += (a*b)

if check == total:
    print('Yes')
else:
    print('No')
  
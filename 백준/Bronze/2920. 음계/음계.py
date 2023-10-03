import sys

scales = [int(i) for i in sys.stdin.readline().rstrip().split()]
asceding = [1,2,3,4,5,6,7,8]
descending= [8,7,6,5,4,3,2,1]

if scales == asceding:
  print('ascending')
elif scales == descending:
  print('descending')
else:
  print('mixed')
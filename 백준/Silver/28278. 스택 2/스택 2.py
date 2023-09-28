import sys

rep = int(sys.stdin.readline().rstrip())
stack = []

for _ in range(rep):
  comm = sys.stdin.readline().rstrip()

  if '1' in comm:
    comm, num = comm.split()
    stack.append(int(num))

  elif '2' in comm:
    if len(stack):
      print(stack.pop(-1))
    else:
      print(-1)

  elif '3' in comm:
    print(len(stack))

  elif '4' in comm:
    if not len(stack):
      print(1)
    else:
      print(0)

  else:
    if len(stack):
      print(stack[-1])
    else:
      print(-1)
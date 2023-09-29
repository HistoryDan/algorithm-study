from collections import deque
import sys

rep = int(sys.stdin.readline().rstrip())
queue = deque()

for _ in range(rep):
  comm = sys.stdin.readline().rstrip()
  
  if 'push' in comm:
    comm, n = comm.split()
    queue.append(int(n))
    
  elif 'pop' in comm:
    if len(queue):
      print(queue.popleft())
    else:
      print(-1)

  elif 'size' in comm:
    print(len(queue))

  elif 'empty' in comm:
    if not len(queue):
      print(1)
    else:
      print(0)

  elif 'front' in comm:
    if len(queue):
      print(queue[0])
    else:
      print(-1)
      
  else:
    if len(queue):
      print(queue[-1])
    else:
      print(-1)
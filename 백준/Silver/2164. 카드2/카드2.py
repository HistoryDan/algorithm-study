from collections import deque
import sys

rep = int(sys.stdin.readline().rstrip())
queue = deque(range(1,rep+1))

while len(queue) > 1:
  queue.popleft()
  temp = queue.popleft()
  queue.append(temp)

print(*queue)
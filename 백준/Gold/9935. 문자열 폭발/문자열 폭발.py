import sys 
from collections import deque

string = input().rstrip()
bomb = input().rstrip()
last = bomb[-1]
stack = deque()

for s in string:
    stack.append(s)
    if s == last and len(stack) >= len(bomb) and ''.join([stack[i] for i in range(-len(bomb),0)]) == bomb:
        for _ in range(len(bomb)):
            stack.pop()

if stack:
    print(''.join(stack))
else:
    print('FRULA')
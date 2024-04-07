import sys
from collections import deque

T = int(input())
for _ in range(T):
    keys = input().rstrip()
    left = deque()
    right = deque()

    for key in keys:
        if key.isalnum():
            left.append(key)
        elif key == '<':
            if left:
                right.appendleft(left.pop())
        elif key == '>':
            if right:
                left.append(right.popleft())
        else: # key is '-'
            if left:
                left.pop()

    print(''.join(left)+''.join(right))
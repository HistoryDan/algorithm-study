import sys 
from collections import deque

def move_left(queue):
    new = [queue[i+1] for i in range(len(queue)-1)] + [queue[0]]
    return new

def move_right(queue):
    new = [queue[-1]] + [queue[i-1] for i in range(1,len(queue))]
    return new

# initialization
n,m = map(int, sys.stdin.readline().rstrip().split())
targets = [int(i) for i in sys.stdin.readline().rstrip().split()]
queue = [i for i in range(1,n+1)]
cnt = 0
target = targets[0]

# count moves
while targets:
    front = queue[0]
    if front == target:
        queue.remove(target)
        targets.remove(target)
        if targets: target = targets[0]

    elif queue.index(target) > len(queue) // 2:
        for _ in range(len(queue) - queue.index(target)):
            queue = move_right(queue)
            # print(queue)
            cnt += 1

    else:
        for _ in range(queue.index(target)):
            queue = move_left(queue)
            # print(queue)
            cnt += 1

print(cnt)
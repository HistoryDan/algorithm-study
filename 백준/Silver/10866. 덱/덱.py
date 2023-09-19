#10866 덱
import sys

deque = []
num_cmds = int(input())

for i in range(num_cmds):
    cmd = sys.stdin.readline().strip()
    
    if 'push_front' in cmd:
        _, element = cmd.split()
        deque.insert(0,element)
    elif 'push_back' in cmd:
        _, element = cmd.split()
        deque.insert(len(deque), element)
    elif 'pop_front' in cmd:
        if len(deque):
            print(deque.pop(0))
        else:
            print(-1)
    elif 'pop_back' in cmd:
        if len(deque):
            print(deque.pop(-1))
        else:
            print(-1)
    elif 'size' in cmd:
        print(len(deque))
    elif 'empty' in cmd:
        if len(deque):
            print(0)
        else:
            print(1)
    elif 'front' in cmd:
        if len(deque):
            print(deque[0])
        else:
            print(-1)
    else:
        if len(deque):
            print(deque[-1])
        else:
            print(-1)
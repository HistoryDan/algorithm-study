#10845 큐
import sys

queue = []
num_cmds = sys.stdin.readline()
num_cmds = int(num_cmds)

for i in range(num_cmds):
    cmd = sys.stdin.readline()
    if 'push' in cmd:
        _, element = cmd.split()
        queue.append(element)
    elif 'pop' in cmd:
        if len(queue):
            print(queue.pop(0))
        else:
            print(-1)
    elif 'size' in cmd:
        print(len(queue))
    elif 'empty' in cmd:
        if len(queue):
            print(0)
        else:
            print(1)
    elif 'front' in cmd:
        if len(queue):
            print(queue[0])
        else:
            print(-1)
    else:
        if len(queue):
            print(queue[-1])
        else:
            print(-1)
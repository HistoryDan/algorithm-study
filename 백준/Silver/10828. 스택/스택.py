import sys
stack = []
cmds = int(input())

for i in range(cmds):
    cmd = sys.stdin.readline()
    
    if 'push' in cmd:
        stack.append(int(cmd.split()[-1]))
    elif 'pop' in cmd:
        if len(stack):
            print(stack.pop())
        else:
            print(-1)
    elif 'size' in cmd:
        print(len(stack))
    elif 'empty' in cmd:
        if len(stack) > 0:
            print(0)
        else: 
            print(1)
    else:
        if len(stack):
            print(stack[-1])
        else:
            print(-1)
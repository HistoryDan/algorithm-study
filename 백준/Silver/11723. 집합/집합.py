import sys

def add(s,x):
    s.add(x)

def remove(s,x):
    if x in s:
        s.remove(x)

def check(s,x):
    if x in s: print(1)
    else: print(0)

def toggle(s,x):
    if x in s: s.remove(x)
    else: s.add(x)

def all(s):
    s = set()
    for i in range(1,21):
        s.add(i)
    return s

def empty(s):
    s = set()
    return s

m = int(sys.stdin.readline())
s = set()
for _ in range(m):
    command = sys.stdin.readline().rstrip()
    if command == 'all': s = all(s)
    elif command == 'empty': s = empty(s)
    else:
        command, x = command.split()
        x = int(x)
        if command == 'add': add(s,x)
        elif command == 'check': check(s,x)
        elif command == 'remove': remove(s,x)
        else: toggle(s,x)



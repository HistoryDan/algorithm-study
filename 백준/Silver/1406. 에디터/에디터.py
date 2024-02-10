import sys 
input = sys.stdin.readline

left = [s for s in input().rstrip()]
right = []
m = int(input().rstrip())

for _ in range(m):
    command = input().rstrip()
    if 'L' == command[0] and left:
        right.append(left.pop())
    elif 'D' == command[0] and right:
        left.append(right.pop())
    elif 'B' == command[0] and left:
        left.pop()
    elif 'P' == command[0]:
        _, new_char = command.split()
        left.append(new_char)
        
right = reversed(right)
print(''.join(left) + ''.join(right))
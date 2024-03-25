import sys 
from collections import deque

expression = input().rstrip()
expression1 = [c for c in expression]
stack = deque()

# validation check
for exp in expression:
    if exp == '(' or exp == '[':
        stack.append(exp)
    elif exp == ')':
        if stack and stack[-1] == '(':
            stack.pop()
        else:
            print(0)
            sys.exit()
    else:
        if stack and stack[-1] == '[':
            stack.pop()
        else:
            print(0)
            sys.exit()
if stack:
    print(0)
    sys.exit()
    
# calculation
expression = expression.replace('()', '2')
expression = expression.replace('[]', '3')
expression2 = [c for c in expression]

for exp in expression2:
    if exp == '(' or exp == '[' or exp.isnumeric():
        stack.append(exp)
    elif exp == ']':
        temp = 0
        top = stack.pop()
        while top != '[':
            temp += int(top)
            top = stack.pop()
        stack.append(str(3*temp))
    elif exp == ')':
        temp = 0
        top = stack.pop()
        while top != '(':
            temp += int(top)
            top = stack.pop()
        stack.append(str(2*temp))

answer = 0
for num in stack:
    answer += int(num)
print(answer)
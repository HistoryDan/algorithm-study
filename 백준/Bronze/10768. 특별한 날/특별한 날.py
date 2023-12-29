import sys

month = int(sys.stdin.readline().rstrip())
day = int(sys.stdin.readline().rstrip())

if month < 2 : print('Before')
elif month > 2 : print('After')
else:
    if day < 18 : print('Before')
    elif day > 18 : print('After')
    else: print('Special')
import sys

while True:
    num = sys.stdin.readline().rstrip()
    if num == '0':
        break
    rev = num[::-1]
    if num == rev:
        print('yes')
    else:
        print('no')
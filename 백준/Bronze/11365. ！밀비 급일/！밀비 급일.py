import sys

while True:
    line = sys.stdin.readline().rstrip()
    if line == 'END':
        break
    line = line[::-1]
    print(line)
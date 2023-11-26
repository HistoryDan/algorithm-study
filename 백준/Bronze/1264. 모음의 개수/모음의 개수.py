import sys 
while True:
    line = sys.stdin.readline().rstrip()
    if line == '#':
        break
    count = line.count('a') + line.count('e') + line.count('i') + line.count('o') + line.count('u') \
    + line.count('A') + line.count('E') + line.count('I') + line.count('O') + line.count('U')
    print(count)
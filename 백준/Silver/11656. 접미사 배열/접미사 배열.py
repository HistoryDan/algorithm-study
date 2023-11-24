import sys 
string = sys.stdin.readline().rstrip()
prefix = []
for i in range(len(string)):
    prefix.append(string[i:])
prefix = sorted(prefix)
for p in prefix:
    print(p)
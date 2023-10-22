import sys
n = int(sys.stdin.readline().rstrip())
sentences = []

for i in range(n):
    s = sys.stdin.readline().rstrip()
    sentences.append(str(i+1)+". "+s)

for s in sentences:
    print(s)
import sys 

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    key1 = sys.stdin.readline().rstrip().split()
    key2 = sys.stdin.readline().rstrip().split()
    cipher  = sys.stdin.readline().rstrip().split()
    answer = []
    for key in key1:
        answer.append(cipher[key2.index(key)])
    print(*answer)

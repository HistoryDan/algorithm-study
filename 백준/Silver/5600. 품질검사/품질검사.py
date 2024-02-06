import sys

a,b,c = map(int, sys.stdin.readline().rstrip().split())
n = int(sys.stdin.readline().rstrip())
checks = []
answers = [2] * (a+b+c+1)

for _ in range(n):
    i,j,k,r = map(int, sys.stdin.readline().rstrip().split())
    checks.append((i,j,k,r))

# find goods
for check in checks:
    if check[3] == 1:
        i,j,k,_ = check
        answers[i] = answers[j] = answers[k] = 1
    
# find bads
for check in checks:
    if check[3] == 0:
        i,j,k,_ = check
        if answers[i] == 1 and answers[j] == 1:
            answers[k] = 0
        elif answers[j] == 1 and answers[k] == 1:
            answers[i] = 0
        elif answers[k] == 1 and answers[i] == 1:
            answers[j] = 0

for i in range(1,len(answers)):
    print(answers[i])
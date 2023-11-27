import sys 
n = sys.stdin.readline().rstrip()
notFound = True
for i in range(1,len(n)):
    front = back = 1
    for j in range(i):
        front *= int(n[j])
    for k in range(i,len(n)):
        back *= int(n[k])
    if front == back:
        print('YES')
        notFound = False
        break
if notFound:
    print('NO')
    
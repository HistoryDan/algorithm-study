import sys 

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    a,b = sys.stdin.readline().rstrip().split()
    ref = [0 for _ in range(26)]
    flag = True

    for i in range(len(a)):
        ref[ord(a[i])-97] += 1

    for i in range(len(b)):
        ref[ord(b[i])-97] -= 1
    
    for r in ref:
        if r != 0:
            flag = False
            break

    if flag:
        print('Possible')
    else:
        print('Impossible')
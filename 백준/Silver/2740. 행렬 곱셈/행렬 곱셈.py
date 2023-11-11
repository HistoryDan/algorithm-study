import sys
a = []
b = []
c = []
n,m = map(int, sys.stdin.readline().rstrip().split())

for _ in range(n):
    row =  list(map(int, sys.stdin.readline().rstrip().split()))
    a.append(row)

m,k = map(int, sys.stdin.readline().rstrip().split())

for _ in range(m):
    row =  list(map(int, sys.stdin.readline().rstrip().split()))
    b.append(row)

for i in range(n):
    for j in range(k):
        element = 0
        for l in range(m):
            element += (a[i][l]*b[l][j])
        print(element, end = ' ')
    print()



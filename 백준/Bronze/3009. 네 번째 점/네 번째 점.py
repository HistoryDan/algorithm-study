import sys
xs = []
ys = []

for _ in range(3):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    xs.append(x)
    ys.append(y)

def findrest(xs):
    for x in xs:
        if xs.count(x) == 1:
            return x

answer = []
answer.append(findrest(xs))
answer.append(findrest(ys))

print(*answer)
    


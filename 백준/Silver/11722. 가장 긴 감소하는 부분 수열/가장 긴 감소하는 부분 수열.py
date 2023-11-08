import sys

n = int(sys.stdin.readline().rstrip())
a = [int(i) for i in sys.stdin.readline().rstrip().split()]
a.insert(0, 1001)
d = [1001]

for i in range(1, n+1):
    current = a[i]
    idx = 0
    while (idx < len(d)) and (current < d[idx]):
        idx += 1

    if idx >= len(d):
        d.append(current)
    else:
        d[idx] = current

print(len(d)-1)

    
    

    
import sys 

seq = [1,1,2,4]
for i in range(4, 70):
    new = seq[i-1] + seq[i-2] + seq[i-3] + seq[i-4]
    seq.append(new)

rep = int(sys.stdin.readline())

for _ in range(rep):
    n = int(sys.stdin.readline())
    print(seq[n])
import sys 
seq = [0,1]
n = int(sys.stdin.readline())
if n==0:
    print(0)
elif n==1:
    print(1)
else:
    for i in range(2,n+1):
        new = seq[i-1] + seq[i-2]
        seq.append(new)

    print(seq[-1])

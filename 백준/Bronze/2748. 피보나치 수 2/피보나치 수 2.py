import sys

n = int(sys.stdin.readline())
seq = [0,1]

if n == 0:
    answer = 0
elif n == 1:
    answer = 1
else:
    for i in range(2,n+1):
        seq.append(seq[i-1]+seq[i-2])

answer = seq[n]
print(answer)
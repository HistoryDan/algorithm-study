import sys 

seq = []
i = 1
while len(seq) <= 1000:
    temp = [i] * i
    seq.extend(temp)
    i += 1

a,b = map(int, sys.stdin.readline().rstrip().split())

print(sum(seq[a-1:b]))
    
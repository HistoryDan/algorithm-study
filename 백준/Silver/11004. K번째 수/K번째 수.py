import sys 
n,k=map(int, sys.stdin.readline().split())
seq =  [int(num) for num in sys.stdin.readline().split()]
seq = sorted(seq)

print(seq[k-1])

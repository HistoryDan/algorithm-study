from itertools import permutations
import sys

n = int(sys.stdin.readline())
seq = [i for i in range(1, n+1)]

for permu in permutations(seq, n):
    print(*permu)
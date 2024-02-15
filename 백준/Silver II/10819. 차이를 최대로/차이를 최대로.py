import sys
from itertools import permutations

n = int(sys.stdin.readline())
seq = list(map(int, sys.stdin.readline().split()))
largest = 0

for comb in permutations(seq, n):
    temp = 0
    for i in range(n-1):
        temp += abs(comb[i] - comb[i+1])

    if largest < temp:
        largest = temp

print(largest)
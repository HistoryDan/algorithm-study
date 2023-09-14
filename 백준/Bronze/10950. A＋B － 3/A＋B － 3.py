import sys

iteration = int(input())
for i in range(iteration):
    a,b = map(int, sys.stdin.readline().strip().split())
    print(a+b)
import sys
n = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().rstrip().split()))
B = list(map(int, sys.stdin.readline().rstrip().split()))

A = sorted(A)
B = sorted(B, reverse= True)
answer = 0
for i in range(n):
    answer += A[i] * B[i]

print(answer)
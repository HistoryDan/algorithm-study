import sys

t = int(sys.stdin.readline().rstrip())
zeros = [1] + [0 for _ in range(45)]
ones = [0, 1] + [0 for _ in range(45)]

for i in range(2, 45):
    zeros[i] = zeros[i-1] + zeros[i-2]
    ones[i] = ones[i-1] + ones[i-2]

for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    print(zeros[n], ones[n])
import sys
n = int(sys.stdin.readline().rstrip())

result = [0 for _ in range(10001)]

for i in range(n):
    num = int(sys.stdin.readline().rstrip())
    result[num] += 1

for i,r in enumerate(result):
    for r in range(r):
        print(i)
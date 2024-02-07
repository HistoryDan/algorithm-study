import sys 

n = int(sys.stdin.readline().rstrip())
nums = [int(i) for i in sys.stdin.readline().rstrip().split()]
d = [0] * n

for i in range(n):
    temp = 0
    for j in range(i):
        if nums[j] < nums[i] and d[j] > temp:
            temp = d[j]
    d[i] = temp + 1

print(max(d))
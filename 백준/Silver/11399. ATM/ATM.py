import sys 
n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
nums = sorted(nums)
answer = 0

for i in range(n):
    answer += sum(nums[:i+1])

print(answer)


import sys 

n = int(sys.stdin.readline().rstrip())
nums = [int(i) for i in sys.stdin.readline().rstrip().split()]
x = int(sys.stdin.readline().rstrip())
ref = [0 for _ in range(2000005)]

for num in nums:
    ref[num] += 1

answer = 0

if x % 2 == 0:
    for i in range(1, x//2):
        answer += (ref[i]*ref[x-i]) 
    answer += (ref[x//2] * (ref[x//2]-1)) // 2
else:
    for i in range(1, x//2+1):
        answer += (ref[i]*ref[x-i])

print(answer)
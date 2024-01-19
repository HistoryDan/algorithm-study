import sys 
from itertools import permutations

n = int(sys.stdin.readline().rstrip())
nums = [int(i) for i in sys.stdin.readline().rstrip().split()]
answer = [0] * n

for i in range(n):
    cnt = 0
    for j in range(n):
        if cnt == nums[i] and answer[j] == 0:
            answer[j] = i + 1
            break
        elif answer[j] == 0:
            cnt += 1

print(*answer)
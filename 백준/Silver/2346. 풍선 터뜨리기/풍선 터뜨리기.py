from collections import deque

N = int(input())
nums = [(int(num), idx+1) for idx, num in enumerate(input().rstrip().split())]
nums = deque(nums)
answers = [1]

cur_n, _ = nums.popleft()
while nums:
    if cur_n > 0:
        for _ in range(cur_n-1):
            nums.append(nums.popleft())
        cur_n, cur_i = nums.popleft()
    else:
        for _ in range(abs(cur_n)-1):
            nums.appendleft(nums.pop())
        cur_n, cur_i = nums.pop()
    answers.append(cur_i)

print(*answers)
import sys 
from collections import deque

N = int(input())
nums = [int(i) for i in input().split()]
answers = [[0,0,0] for _ in range(N+1)] # count, left nearest index, right nearest index
stack = deque()

for i,num in enumerate(nums):
    count = 0
    left_idx = -1
    while stack and stack[-1][1] <= num:
        stack.pop()
    if stack:
        count = len(stack)
        left_idx = stack[-1][0]
    stack.append((i+1, num))
    answers[i+1][0] += count
    answers[i+1][1] = left_idx
    
stack.clear()
for i,num in enumerate(nums[::-1]):
    count = 0
    right_idx = -1
    while stack and stack[-1][1] <= num:
        stack.pop()
    if stack:
        count = len(stack)
        right_idx = stack[-1][0]
    stack.append((N-i, num))
    answers[N-i][0] += count 
    answers[N-i][2] = right_idx

for i in range(1, len(answers)):
    count, left_idx, right_idx = answers[i]
    if count == 0:
        print(0)
    elif left_idx == -1:
        print(count, right_idx)
    elif right_idx == -1:
        print(count, left_idx)
    else:
        left_diff = abs(i-left_idx)
        right_diff = abs(i-right_idx)
        if left_diff <= right_diff:
            print(count, left_idx)
        else:
            print(count, right_idx)
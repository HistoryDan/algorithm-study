from collections import deque

N = int(input())
towers = [(int(n),i) for i, n in enumerate(input().split())]
stack1 = deque(towers[:-1])
stack2 = deque()
stack2.append(towers[-1])

answers = [0] * N
while stack1:
    while stack2 and stack1[-1][0] > stack2[-1][0]:
        answers[stack2[-1][1]] = stack1[-1][1] + 1
        stack2.pop()
    stack2.append(stack1.pop())

print(*answers)
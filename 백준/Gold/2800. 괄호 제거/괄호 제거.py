from collections import deque
from itertools import combinations

exp = input().rstrip()
stack = deque()
pairs = []
# (()())
for i, c in enumerate(exp):
    if c == '(' :
        stack.append(i)
    elif c == ')':
        popped = stack.pop()
        pairs.append((popped, i))

answers = []
for i in range(1,len(pairs)+1):
    for comb in combinations(pairs, i):
        indices = []
        for pair in comb:
            indices.extend(pair)
        answer = []
        for i, e in enumerate(exp):
            if i in indices:
                continue
            else:
                answer.append(e)
        answer = ''.join(answer)
        answers.append(answer)

answers = set(answers)
answers = sorted(answers)
for answer in answers:
    print(answer)
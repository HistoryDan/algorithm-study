import sys 
from itertools import product
input = sys.stdin.readline

M,N = map(int, input().split())
nums = [int(i) for i in input().split()]
nums.sort()
answers = set()

if N == 1:
    for i in range(M):
        answers.add((nums[i],))

elif N == 2:
    for i in range(M):
        for j in range(i,M):
            answers.add((nums[i], nums[j]))

elif N == 3:
    for i in range(M):
        for j in range(i,M):
            for a in range(j,M):
                answers.add((nums[i], nums[j], nums[a]))

elif N == 4:
    for i in range(M):
        for j in range(i,M):
            for a in range(j,M):
                for b in range(a,M):
                    answers.add((nums[i], nums[j],nums[a],nums[b]))

elif N == 5:
    for i in range(M):
        for j in range(i,M):
            for a in range(j,M):
                for b in range(a,M):
                    for c in range(b,M):
                        answers.add((nums[i], nums[j],nums[a], nums[b], nums[c]))

elif N == 6:
    for i in range(M):
        for j in range(i,M):
            for a in range(j,M):
                for b in range(a,M):
                    for c in range(b,M):
                        for d in range(c,M):
                            answers.add((nums[i], nums[j],nums[a], nums[b], nums[c], nums[d]))

elif N == 7:
    for i in range(M):
        for j in range(i,M):
            for a in range(j,M):
                for b in range(a,M):
                    for c in range(b,M):
                        for d in range(c,M):
                            for e in range(d,M):
                                answers.add((nums[i], nums[j],nums[a], nums[b], nums[c], nums[d], nums[e]))


else:
    for i in range(M):
        for j in range(i,M):
            for a in range(j,M):
                for b in range(a,M):
                    for c in range(b,M):
                        for d in range(c,M):
                            for e in range(d,M):
                                for f in range(e,M):
                                    answers.add((nums[i], nums[j],nums[a], nums[b], nums[c], nums[d], nums[e], nums[f]))

answers = sorted(list(answers))
for answer in answers:
    print(*answer)
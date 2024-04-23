import sys 
from itertools import permutations
input = sys.stdin.readline

N = int(input())
costs = []
for _ in range(N):
    row = [int(i) for i in input().split()]
    costs.append(row)
cities = [i for i in range(N)]

answer = 1e9
for permu in permutations(cities):
    temp = 0
    flag = True
    for i in range(1,N+1):
        depart, arrive = permu[i-1], permu[i%N]
        cost = costs[depart][arrive]
        if cost == 0:
            flag = False
            break
        temp += cost
        if temp > answer: break
    if flag and temp < answer:
        answer = temp

print(answer)
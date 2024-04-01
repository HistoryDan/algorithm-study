import sys
from itertools import combinations
input = sys.stdin.readline

def city_chicken_distance(houses, chickens):
    result = []
    for house in houses:
        shortest_dist = float('inf')
        for chicken in chickens:
            dist = abs(house[0] - chicken[0]) + abs(house[1] - chicken[1])
            if dist < shortest_dist:
                shortest_dist = dist
        result.append(shortest_dist)
    return sum(result)

N,M = map(int, input().split())
graph = []
for _ in range(N):
    row = [int(i) for i in input().split()]
    graph.append(row)

chickens = []
houses = []
for r in range(N):
    for c in range(N):
        if graph[r][c] == 2:
            chickens.append((r,c))
        elif graph[r][c] == 1:
            houses.append((r,c))

shortest_city_dist = float('inf')
for comb in combinations(chickens, M):
    cur_dist = city_chicken_distance(houses, comb)
    if cur_dist < shortest_city_dist:
        shortest_city_dist = cur_dist

print(shortest_city_dist)
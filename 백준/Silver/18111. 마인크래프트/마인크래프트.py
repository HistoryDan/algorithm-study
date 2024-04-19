import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())
ground = []
for _ in range(N):
    row = [int(i) for i in input().split()]
    ground.extend(row)

highest = max(ground)
lowest = min(ground)

cost = float('inf')
height = -1
flag = True
ground.sort(reverse=True)
for i in range(lowest,highest+1):
    temp_cost = 0
    temp_height = i
    invent = B
    for j in range(N*M):
        if ground[j] > temp_height:
            temp_cost += (ground[j] - temp_height) * 2
            invent += (ground[j] - temp_height)
        elif ground[j] < temp_height:
            temp_cost += (temp_height - ground[j])
            invent -= (temp_height - ground[j])
            if invent < 0:
                flag = False
                break
    if flag:
        if temp_cost <= cost:
            cost = temp_cost
            height = temp_height

print(cost, height)
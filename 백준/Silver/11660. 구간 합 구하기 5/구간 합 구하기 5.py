import sys 
input = sys.stdin.readline

def calculate_sum(x1,y1,x2,y2):
    result = 0
    for i in range(x1,x2+1):
        if y1 == 0:
            result += (graph[i][y2])
        else:
            result += (graph[i][y2] - graph[i][y1-1])
    return result

N,M = map(int, input().split())
graph = []
for _ in range(N):
    nums = [int(i) for i in input().split()]
    row = [0]*N
    for i in range(N):
        row[i] = sum(nums[:i+1])
    graph.append(row)

for _ in range(M):
    x1,y1,x2,y2 = map(int, input().split())
    print(calculate_sum(x1-1,y1-1,x2-1,y2-1))
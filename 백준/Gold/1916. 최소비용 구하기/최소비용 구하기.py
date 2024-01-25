import sys

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
graph = [[sys.maxsize for _ in range(n)] for _ in range(n)]

for _ in range(m):
    s,d,c = map(int, sys.stdin.readline().rstrip().split())
    graph[s-1][d-1] = min(c, graph[s-1][d-1])

for i in range(n):
    for j in range(n):
        if i == j : graph[i][j] = 0

src, dest = map(int, sys.stdin.readline().rstrip().split())
dist = [sys.maxsize] * n
dist[src-1] = 0  # 시작 정점의 거리를 0으로 설정
fix = [0 for _ in range(n)]

# 다익스트라 
while True:
    idx = -1
    # 현재 거리 테이블에서 최소 거리를 가지는 정점 찾기
    for i in range(n):
        if fix[i]: continue
        if idx == -1 : idx = i
        elif dist[i] < dist[idx] : idx = i

    # 최단 거리 찾기가 완료된 경우 반복문 종료
    if idx == -1 or dist[idx] == sys.maxsize:
        break
    
    # 현재 거리 테이블에서 최단 거리를 가지는 정점 fix
    fix[idx] = 1

    # 현재 확정된 정점을 통하여 각 정점을 방문하는 거리 비용 업데이트
    for i in range(n):
        if dist[i] > dist[idx] + graph[idx][i]:
            dist[i] = dist[idx] + graph[idx][i]

print(dist[dest-1])
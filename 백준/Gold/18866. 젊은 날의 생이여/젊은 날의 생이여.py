import sys
input = sys.stdin.readline

N = int(input())
v = [[0, 0] for _ in range(N)]

for i in range(N):
    v1, v2 = map(int, input().split())
    v[i][0] = v1
    v[i][1] = v2

young = [[0, 0] for _ in range(N)]
old = [[0, 0] for _ in range(N)]

max_happy = 0
min_happy = float('inf')
max_tired = 0
min_tired = float('inf')

for i in range(N):
    if min_happy > v[i][0] and v[i][0] != 0:
        min_happy = v[i][0]
    if max_tired < v[i][1] and v[i][1] != 0:
        max_tired = v[i][1]

    young[i][0] = min_happy
    young[i][1] = max_tired

for i in range(N-1, -1, -1):
    if max_happy < v[i][0] and v[i][0] != 0:
        max_happy = v[i][0]
    if min_tired > v[i][1] and v[i][1] != 0:
        min_tired = v[i][1]

    old[i][0] = max_happy
    old[i][1] = min_tired

ans = 0
for i in range(N-1):
    if young[i][0] > old[i+1][0] and young[i][1] < old[i+1][1]:
        ans = i+1

if ans == 0:
    ans = -1

print(ans)
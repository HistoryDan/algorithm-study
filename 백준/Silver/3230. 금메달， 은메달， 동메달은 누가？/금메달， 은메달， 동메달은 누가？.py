import sys

n, m = map(int, sys.stdin.readline().split())
round1 = []


for i in range(1,n+1):
    rank = int(sys.stdin.readline().rstrip())
    round1.insert(rank-1,i)

round2 = round1[:m][::-1]
answer = []
for i in range(m):
    rank = int(sys.stdin.readline().rstrip())
    answer.insert(rank-1, round2[i])

for i in range(3):
    print(answer[i])
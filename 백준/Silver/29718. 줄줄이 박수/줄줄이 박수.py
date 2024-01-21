import sys 

n,m = map(int, sys.stdin.readline().rstrip().split())
clap_mat = []
for _ in range(n):
    row = [int(i) for i in sys.stdin.readline().rstrip().split()]
    clap_mat.append(row)
a = int(sys.stdin.readline().rstrip())

ref = [0 for _ in range(m)]
for i in range(m):
    sum_ = 0
    for j in range(n):
        sum_ += clap_mat[j][i]
    ref[i] = sum_

answer = 0
for i in range(m-a+1):
    if sum(ref[i:i+a]) > answer:
        answer = sum(ref[i:i+a])

print(answer)

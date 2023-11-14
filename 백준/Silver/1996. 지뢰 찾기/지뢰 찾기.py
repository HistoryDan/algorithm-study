import sys

n = int(sys.stdin.readline())
arr = []

for _ in range(n):
    line = sys.stdin.readline().rstrip()
    row = []
    for i in range(n):
        ele = line[i]
        if ele == '.':
            ele = 0
        row.append(int(ele))
    arr.append(row)

answer = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if arr[i][j] == 0:
            for k in range(i-1, i+2):
                for l in range(j-1, j+2):
                    if (k>=0) and (k<n) and (l>=0) and (l<n):
                        answer[i][j] += arr[k][l]
            if answer[i][j] >= 10:
                answer[i][j] = 'M'
        else:
            answer[i][j] = '*'

for i in range(n):
    for j in range(n):
        print(answer[i][j], end = '')
    print()





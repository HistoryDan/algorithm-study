import sys 
input = sys.stdin.readline

N,M = map(int, input().split())
mat = []
for _ in range(N):
    row = [int(i) for i in input().split()]
    mat.append(row)

# row direction
dp_row = [[0] * M for _ in range(N)]
for i in range(N):
    dp_row[i][0] = mat[i][0]
    for j in range(1, M):
        dp_row[i][j] = dp_row[i][j-1] + mat[i][j]

# column direction
dp_col = [[0] * M for _ in range(N)]
for j in range(M):
    dp_col[0][j] = mat[0][j]
    for i in range(1, N):
        dp_col[i][j] = dp_col[i-1][j] + mat[i][j]

K = int(input())
for _ in range(K):
    i,j,x,y = map(int, input().split())
    i -= 1
    j -= 1
    x -= 1
    y -= 1
    answer = 0
    if i == x and j != y:
        if j == 0:
            answer = dp_row[x][y]
        else:
            answer = dp_row[x][y] - dp_row[i][j-1]
    elif i != x and j == y:
        if i == 0:
            answer = dp_col[x][y]
        else:
            answer = dp_col[x][y] - dp_col[i-1][j]
    elif i == x and j == y:
        answer = mat[x][y]
    else:
        if j == 0:
            for k in range(i,x+1):
                answer += dp_row[k][y]
        else:
            for k in range(i,x+1):
                answer += (dp_row[k][y] - dp_row[k][j-1])
    print(answer)
import sys
input = sys.stdin.readline

def check(num):
    '''Return True if num is a perfect square number'''
    q = num ** (0.5)
    return q % 1 == 0

N, M = map(int, input().split())
matrix = [[int(i) for i in input().rstrip()] for _ in range(N)] 
drs = [i for i in range(N)] + [-i for i in range(1,N)]    
dcs = [i for i in range(M)] + [-i for i in range(1,M)]    
cands = set()

for i in range(N):
    for j in range(M):
        for dr in drs:
            for dc in dcs:
                if dr == 0 and dc == 0:
                    num = matrix[i][j]
                    if check(num): cands.add(num)
                else:
                    num = 0
                    r, c = i, j
                    while 0 <= r < N and 0 <= c < M:
                        num = num * 10 + matrix[r][c]
                        if check(num):
                            cands.add(num)
                        r += dr
                        c += dc 

print(max(cands) if cands else -1)      
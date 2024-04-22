import sys 
import copy
from itertools import permutations
input = sys.stdin.readline

def get_value(matrix):
    value = float('inf')
    for row in matrix:
        if value > sum(row):
            value = sum(row)
    return value

def rotate(matrix, r,c,s):
    top, left, bottom, right = r-s, c-s, r+s, c+s
    top_left, top_right = matrix[top][left], matrix[top][right]
    bottom_left, bottom_right = matrix[bottom][left], matrix[bottom][right]

    for i in range(2*s,0,-1):
        matrix[top][left+i] = matrix[top][left+i-1]

    for i in range(2*s):
        matrix[top+i][left] = matrix[top+i+1][left]

    for i in range(2*s):
        matrix[bottom][left+i] = matrix[bottom][left+i+1]

    for i in range(2*s,0,-1):
        matrix[top+i][right] = matrix[top+i-1][right]

    matrix[top+i][right] = top_right

# def output(matrix):
#     print()
#     for row in matrix:
#         print(*row)
#     print()

N,M,K = map(int, input().split())
matrix = []
for _ in range(N):
    row = [int(i) for i in input().split()]
    matrix.append(row)

operations = []
answer = float('inf')
for _ in range(K):
    r,c,s = map(int, input().split())
    r -= 1
    c -= 1
    operations.append((r,c,s))

for permu in permutations(operations):
    temp = copy.deepcopy(matrix)
    for r,c,s in permu:
        for i in range(1,s+1):
            rotate(temp,r,c,i)
    if get_value(temp) < answer:
        answer = get_value(temp)

print(answer)
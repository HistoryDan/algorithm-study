import sys 
input = sys.stdin.readline

N = int(input())
tree = []
for _ in range(N):
    row = [int(i) for i in input().split()]
    tree.append(row)

ref_tree = [[0]*i for i in range(1,N+1)]
ref_tree[0][0] = tree[0][0]

for i in range(N-1):
    for j in range(len(tree[i])):
        current = ref_tree[i][j]
        left = tree[i+1][j] + current
        right = tree[i+1][j+1] + current
        if left > ref_tree[i+1][j]:
            ref_tree[i+1][j] = left
        if right > ref_tree[i+1][j+1]:
            ref_tree[i+1][j+1] = right

print(max(ref_tree[-1]))
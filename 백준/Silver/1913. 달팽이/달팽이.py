import sys 

def make_surface(snail, first):

    size_snail = len(snail[0])
    size_surface = int(first**0.5)
    start = (size_snail - size_surface) // 2
    
    for i in range(size_surface):
        snail[start+i][start] = first
        first -= 1
    
    for i in range(size_surface-1):
        snail[start+size_surface-1][start+i+1] = first
        first -= 1
    
    for i in range(size_surface-1):
        snail[start+size_surface-i-2][start+size_surface-1] = first
        first -= 1

    for i in range(size_surface-2):
        snail[start][start+size_surface-2-i] = first
        first -= 1


n = int(sys.stdin.readline().rstrip())
target = int(sys.stdin.readline().rstrip())
snail = [[0 for _ in range(n)] for _ in range(n)]
target_index = []
for i in range(1,n+1,2):
    make_surface(snail, i**2)

for i in range(n):
    for j in range(n):
        print(snail[i][j], end= ' ')
        if snail[i][j] == target: target_index.extend([i+1,j+1])
    print()

print(*target_index)
import sys 

n = int(sys.stdin.readline().rstrip())
for _ in range(n):
    letters = sys.stdin.readline().rstrip()
    size = int(len(letters)**0.5)
    arr = [[0 for _ in range(size)] for _ in range(size)]

    for i in range(size):
        for j in range(size):
            arr[i][j] = letters[size*i+j]
    
    for i in range(size-1,-1,-1):
        for j in range(size):
            print(arr[j][i], end='')

    print()

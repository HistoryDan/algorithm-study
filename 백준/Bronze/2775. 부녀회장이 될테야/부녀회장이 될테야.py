import sys

arr = [[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]]
for i in range(1,15):
    arr.append([0 for _ in range(15)])
    for j in range(14):
        arr[i][j] = sum(arr[i-1][:j+1])

rep = int(sys.stdin.readline().rstrip())

for _ in range(rep):
  k = int(sys.stdin.readline().rstrip())
  n = int(sys.stdin.readline().rstrip())
  
  print(arr[k][n-1])
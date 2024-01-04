import sys 
x,y = sys.stdin.readline().rstrip().split()
x = int(x[::-1])
y = int(y[::-1])
answer = int(str(x + y)[::-1])

print(answer)
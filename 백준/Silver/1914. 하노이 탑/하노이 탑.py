import sys 
sys.setrecursionlimit(10**6)

def hanoi1(x,y,z,n):
    global cnt
    if n > 0:
        hanoi1(x,z,y,n-1)
        print(x,z)
        hanoi1(y,x,z,n-1)

n = int(sys.stdin.readline().rstrip())

print(2**n-1)
if n <= 20:
    hanoi1(1,2,3,n)
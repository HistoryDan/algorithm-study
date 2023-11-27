import sys 
delay = 0
for _ in range(4):
    sec = int(sys.stdin.readline())
    delay += sec
print(delay//60)
print(delay%60)
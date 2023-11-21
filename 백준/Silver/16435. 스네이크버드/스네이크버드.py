import sys 
n,l = map(int, sys.stdin.readline().split())
heights = list(map(int, sys.stdin.readline().split()))
heights = sorted(heights)

for height in heights:
    if height <= l:
        l+=1
    else:
        break
print(l)

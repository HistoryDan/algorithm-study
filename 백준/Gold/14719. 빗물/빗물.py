import sys 
input = sys.stdin.readline

h,w = map(int, input().rstrip().split())
heights = [int(i) for i in input().rstrip().split()]
total = 0

for i in range(1,w-1):
    right = max(heights[i+1:])
    left = max(heights[:i])
    ref = min(right, left)
    if ref > heights[i]:
        total += (ref - heights[i])

print(total)
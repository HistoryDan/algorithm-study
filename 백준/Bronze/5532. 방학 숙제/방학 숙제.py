import sys
import math

l = int(sys.stdin.readline())
a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())
d = int(sys.stdin.readline())

answer = l - max(math.ceil(a/c), math.ceil(b/d))
print(answer)
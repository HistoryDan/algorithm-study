import sys
s = sys.stdin.readline().rstrip()
t = sys.stdin.readline().rstrip()
if len(s) > len(t):
    short = t
    long = s
else: 
    short = s
    long = t
fs = short * len(long)
fl = long * len(short)

if fs == fl:
    print(1)
else:
    print(0)
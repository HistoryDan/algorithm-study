import sys 
e,s,m = map(int, sys.stdin.readline().split())
if e == 15: e=0
if s == 28: s=0
if m == 19: m=0
year = 1
while (year%15!=e) or (year%28!=s) or (year%19!=m):
    year += 1
print(year)
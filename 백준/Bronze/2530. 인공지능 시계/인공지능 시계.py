import sys

h,m,s = map(int, sys.stdin.readline().rstrip().split())
delay = int(sys.stdin.readline().rstrip())

delay_h = delay // 3600
delay %= 3600
delay_m = delay // 60
delay %= 60
delay_s = delay

h = (h + delay_h)
m = (m + delay_m)
s = (s + delay_s)

if s >= 60 :
    m = m + (s//60)
    s %= 60

if m >= 60:
    h += (m//60)
    m %= 60

h %= 24
print(h,m,s)


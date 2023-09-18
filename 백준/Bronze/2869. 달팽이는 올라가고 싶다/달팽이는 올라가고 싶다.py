a, b, v = map(int, input().split())
oneday = a - b
v -= a

days = v // oneday if v % oneday == 0 else v // oneday + 1

print(days+1)


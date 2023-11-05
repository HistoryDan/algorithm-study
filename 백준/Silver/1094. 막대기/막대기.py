import sys
x = int(sys.stdin.readline().rstrip())
sticks = [64]

while (sum(sticks) != x):
    if sum(sticks) > x:
        shortest = sticks[-1]
        shortest //= 2
        sticks[-1] = shortest
        
        if sum(sticks) >= x :
            pass
        else:
            sticks.append(shortest)


print(len(sticks))

import sys

def isPlayerIn(x,y,w,h,px,py):
    radius = h/2
    if (px>=(x-radius)) and (px<=(x+radius+w)) and (py>=y) and (py<=(y+h)):
        if (px<(x)):
            dist = ((px-x)**2 + (py-(y+radius))**2)**0.5
            if dist <= radius:
                return True
        elif (px>(x+w)):
            dist = (((px-(x+w))**2) + ((py-(y+radius))**2))**0.5
            if dist <= radius:
                return True
        else:
            return True
    return False

w,h,x,y,p = map(int, sys.stdin.readline().split())
count = 0

for _ in range(p):
    px, py = map(int, sys.stdin.readline().split())
    if isPlayerIn(x,y,w,h,px,py):
        count +=1

print(count)
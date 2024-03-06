import sys 
from collections import deque
input = sys.stdin.readline

graph = [[int(i) for i in input().split()] for _ in range(19)]
black_win, white_win = False, False

def west_east(x,y,cur):
    indices = [(x,y)]
    cnt = 1
    nx, ny = x-1, y
    while 0<=nx<19 and 0<=ny<19:
        next = graph[ny][nx]
        if next != cur : break
        cnt += 1
        indices.append((nx,ny))
        nx -= 1

    nx, ny = x+1, y
    while 0<=nx<19 and 0<=ny<19:
        next = graph[ny][nx]
        if next != cur : break
        cnt += 1
        indices.append((nx,ny))
        nx += 1

    return cnt, indices

def north_south(x,y,cur):
    indices = [(x,y)]
    cnt = 1
    nx, ny = x, y-1
    
    while 0<=nx<19 and 0<=ny<19:
        next = graph[ny][nx]
        if next != cur : break
        cnt += 1
        indices.append((nx,ny))
        ny -= 1

    nx, ny = x, y+1
    while 0<=nx<19 and 0<=ny<19:
        next = graph[ny][nx]
        if next != cur : break
        cnt += 1
        indices.append((nx,ny))
        ny += 1
        
    return cnt, indices

def right_diagonal(x,y,cur):
    indices = [(x,y)]
    cnt = 1
    nx, ny = x+1, y-1
    while 0<=nx<19 and 0<=ny<19:
        next = graph[ny][nx]
        if next != cur : break
        cnt += 1
        indices.append((nx,ny))
        ny -= 1
        nx += 1


    nx, ny = x-1, y+1
    while 0<=nx<19 and 0<=ny<19:
        next = graph[ny][nx]
        if next != cur : break
        cnt += 1
        indices.append((nx,ny))
        ny += 1
        nx -= 1
        
    return cnt, indices

def left_diagonal(x,y,cur):
    indices = [(x,y)]
    cnt = 1
    nx, ny = x-1, y-1
    while 0<=nx<19 and 0<=ny<19:
        next = graph[ny][nx]
        if next != cur : break
        cnt += 1
        indices.append((nx,ny))
        ny -= 1
        nx -= 1

    nx, ny = x+1, y+1
    while 0<=nx<19 and 0<=ny<19:
        next = graph[ny][nx]
        if next != cur : break
        cnt += 1
        indices.append((nx,ny))
        ny += 1
        nx += 1
        
    return cnt, indices

for i in range(19):
    for j in range(19):
        cur = graph[i][j]
        if cur != 0:
            cnt1, indices1 = west_east(j,i,cur)
            cnt2, indices2 = north_south(j,i,cur)
            cnt3, indices3 = right_diagonal(j,i,cur)
            cnt4, indices4 = left_diagonal(j,i,cur)
            if 5 in [cnt1, cnt2, cnt3, cnt4]:
                if cur == 1: black_win = True
                elif cur == 2 : white_win = True
        if black_win or white_win: break
    if black_win or white_win: break

if black_win:
    print(1)
    index = [cnt1, cnt2, cnt3, cnt4].index(5)
    indices = [indices1, indices2, indices3, indices4][index]
    indices.sort(key=lambda x: (x[0],x[1]))
    print(indices[0][1]+1, indices[0][0]+1)
elif white_win:
    print(2)
    index = [cnt1, cnt2, cnt3, cnt4].index(5)
    indices = [indices1, indices2, indices3, indices4][index]
    indices.sort(key=lambda x: (x[0],x[1]))
    print(indices[0][1]+1, indices[0][0]+1)
else:
    print(0)
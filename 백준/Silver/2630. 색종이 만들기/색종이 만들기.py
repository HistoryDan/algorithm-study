import sys
input = sys.stdin.readline

def check_color(x,y,l):
    global white_cnt, blue_cnt
    white_flag = blue_flag = 1
    for i in range(x,x+l):
        for j in range(y, y+l):
            if graph[j][i] == 1: white_flag = 0
            else: blue_flag = 0
    if white_flag:
        white_cnt += 1
        return
    elif blue_flag:
        blue_cnt += 1
        return
    else:
        check_color(x,y,l//2)
        check_color(x+l//2,y,l//2)
        check_color(x,y+l//2,l//2)
        check_color(x+l//2,y+l//2,l//2)

n = int(input().rstrip())
graph = [[int(i) for i in input().rstrip().split()] for _ in range(n)]
white_cnt = blue_cnt = 0

check_color(0,0,n)

print(white_cnt)
print(blue_cnt)
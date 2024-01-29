import sys 

def cnt_adj_friends(x,y,n,friends,seats):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    cnt = 0
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and seats[nx][ny] in friends:
            cnt += 1
    return cnt

def cnt_adj_blanks(x,y,n,seats):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    cnt = 0
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and seats[nx][ny]==0:
            cnt += 1
    return cnt

def cal_satisfactory(x,y,n,friends,seats):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    sat = 0
    cnt = 0
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and seats[nx][ny] in friends:
            cnt += 1
    if cnt == 0 : sat = 0
    elif cnt == 1 : sat = 1
    elif cnt == 2 : sat = 10 
    elif cnt == 3 : sat = 100 
    else : sat = 1000
    
    return sat

n = int(sys.stdin.readline().rstrip())
ref = [0]+[0 for _ in range(n*n)]
seats = [[0 for _ in range(n)] for _ in range(n)]
turns = []

for _ in range(n*n):
    line = [int(i) for i in sys.stdin.readline().rstrip().split()]
    idx, friends = line[0], line[1:]
    turns.append(idx)
    ref[idx] = friends

for turn in turns:
    friends = ref[turn]
    # step 1
    first_cands = []
    num_adj_friends = -1
    for i in range(n):
        for j in range(n):
            if seats[i][j] == 0:
                temp = cnt_adj_friends(i,j,n,friends,seats)
                if temp > num_adj_friends:
                    num_adj_friends = temp
                    first_cands = [(i,j)]
                elif temp == num_adj_friends:
                    first_cands.append((i,j))
    # print("Turn:", turn, "first cand:", first_cands)

    # step 2
    second_cands = []
    blank_cnt = -1
    for cand in first_cands:
        i,j = cand
        temp = cnt_adj_blanks(i,j,n,seats)
        if temp > blank_cnt:
            blank_cnt = temp
            second_cands = [(i,j)]
        elif temp == blank_cnt:
            second_cands.append((i,j))
    # print("Turn:", turn, "second cand:", second_cands)

    # step 3 
    sorted_cands = sorted(second_cands, key= lambda x:(x[0],x[1]))
    final_i, final_j = sorted_cands[0]
    seats[final_i][final_j] = turn
    # print("Turn:", turn, "final index:", final_i, final_j)

    # print("Seats:", seats)
    # print()

# step 4
answer = 0
for i in range(n):
    for j in range(n):
        cur = seats[i][j]
        sat = cal_satisfactory(i,j,n, ref[cur],seats)
        answer += sat

print(answer)
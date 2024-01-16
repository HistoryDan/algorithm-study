import sys 

n,m = map(int, sys.stdin.readline().rstrip().split())
street = [int(i) for i in sys.stdin.readline().rstrip().split()]

# first count
first = street[0]
ref = [first] 
cur = first
for i in range(n):
    if street[i] != cur:
        cur = street[i]
        ref.append(cur)
cnt = sum(ref)

# main
for _ in range(m):
    command = sys.stdin.readline().rstrip()
    if command[0] == '0':
        print(cnt)

    else:
        _, idx = map(int, command.split())
        idx -= 1
        if street[idx] == 0:
            if idx == 0:
                if len(street) == 1:
                    cnt += 1
                elif street[1] == 0:
                    cnt += 1
            if idx == n-1:
                if len(street) == 1:
                    cnt += 1
                elif street[n-2] == 0:
                    cnt += 1
            elif street[idx-1] == 0 and street[idx+1] == 0:
                cnt += 1
            elif street[idx-1] == 1 and street[idx+1] == 1:
                cnt -= 1
            street[idx] = 1
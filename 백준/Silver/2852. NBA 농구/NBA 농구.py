import sys 
n = int(sys.stdin.readline().rstrip())
one_score = two_score = 0
scores = []
history = [0 for _ in range(2880)]

for _ in range(n):
    team, time = sys.stdin.readline().rstrip().split()
    if team == '1': one_score += 1
    else: two_score += 1
    idx = int(time[:2])*60 + int(time[3:])

    if one_score > two_score:
        history[idx:] = [1] * (2880-idx)
    elif two_score > one_score:
        history[idx:] = [2] * (2880-idx)
    else:
        history[idx:] = [0] * (2880-idx)

one_winning = two_winning = 0

for h in history:
    if h == 1:
        one_winning += 1
    elif h == 2:
        two_winning += 1

print("{:02d}:{:02d}".format((one_winning//60), (one_winning%60)))
print("{:02d}:{:02d}".format((two_winning//60), (two_winning%60)))
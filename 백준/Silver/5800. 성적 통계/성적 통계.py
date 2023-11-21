import sys 
n = int(sys.stdin.readline())
for k in range(1,n+1):
    scores = list(map(int, sys.stdin.readline().split()))
    scores = sorted(scores[1:], reverse = True)
    largest_gap = 0
    for i in range(len(scores)-1):
        gap = scores[i] - scores[i+1]
        if gap > largest_gap:
            largest_gap = gap
    print('Class', k)
    print('Max '+str(scores[0]) + ', Min '+str(scores[-1])+', Largest gap '+str(largest_gap))

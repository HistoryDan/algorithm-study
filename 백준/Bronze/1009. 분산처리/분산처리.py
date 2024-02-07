import sys 

t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    a,b = map(int, sys.stdin.readline().rstrip().split())
    mod = a % 10
    if mod == 1: ref = [1]
    elif mod == 2: ref = [2,4,8,6]
    elif mod == 3: ref = [3,9,7,1]
    elif mod == 4: ref = [4,6]
    elif mod == 5: ref = [5]
    elif mod == 6: ref = [6]
    elif mod == 7: ref = [7,9,3,1]
    elif mod == 8: ref = [8,4,2,6]
    elif mod == 9: ref = [9,1]
    else: ref = [10]

    print(ref[b%len(ref)-1])
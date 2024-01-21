import sys 

n = int(sys.stdin.readline().rstrip())
ref = [int(i) for i in sys.stdin.readline().rstrip().split()]
m = int(sys.stdin.readline().rstrip())

for _ in range(m):
    answer = [0 for _ in range(n)]
    temp = []
    l,r = map(int, sys.stdin.readline().rstrip().split())
    for i in range(l,r+1):
        idx = ref.index(i)
        temp.append(idx)
    temp.sort()
    first = l
    for t in temp:
        answer[t] = first
        first += 1
    for num in ref:
        if num > r or num < l:
            answer[ref.index(num)] = num
    print(*answer)
import sys

n,k = map(int, sys.stdin.readline().rstrip().split())
seq = [i for i in range(1,n+1)]
answer = []
idx = 0
while len(seq):
    idx += k - 1
    if idx >= len(seq): 
        idx %= len(seq)
    num = seq.pop(idx)
    answer.append(num)

formatted_list = "<" + ", ".join(map(str, answer)) + ">"
print(formatted_list)



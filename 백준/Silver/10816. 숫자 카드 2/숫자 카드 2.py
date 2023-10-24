import sys
_ = int(sys.stdin.readline().rstrip())
nums = sys.stdin.readline().rstrip().split()
count = {}

for n in nums:
    if n in count:
        count[n]+=1
    else:
        count[n] = 1

_ = int(sys.stdin.readline().rstrip())
indices = sys.stdin.readline().rstrip().split()
rslt = []

for i in indices:
    if i in count:
        rslt.append(count[i])
    else:
        rslt.append(0)

print(*rslt)
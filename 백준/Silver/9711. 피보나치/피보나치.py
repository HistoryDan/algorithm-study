import sys 
ref = [1,1] + [0 for _ in range(10000)]
for i in range(2, len(ref)):
    ref[i] = ref[i-1] + ref[i-2]

t = int(sys.stdin.readline().rstrip())
for i in range(t):
    p, q = map(int, sys.stdin.readline().rstrip().split())
    print("Case #{}: {}".format(str(i+1), str(ref[p-1]%q)))

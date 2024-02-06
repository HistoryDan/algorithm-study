import sys 

forest = {}
cnt = 0
while True:
    tree = sys.stdin.readline().rstrip()
    if not tree: break
    cnt += 1
    if tree not in forest.keys():
        forest[tree] = 1
    else:
        forest[tree] += 1

ref = list(forest.keys())
ref.sort()

for r in ref:
    value = (forest[r] / cnt) * 100
    print(f"{r} {value:.4f}")
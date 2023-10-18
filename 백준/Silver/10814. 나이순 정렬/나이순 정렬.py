import sys
n = int(sys.stdin.readline().rstrip())
results = [[] for _ in range(201)]

for _ in range(n):
    age, name = sys.stdin.readline().rstrip().split()
    results[int(age)].append(name)

for i in range(201):
    for j in range(len(results[i])):
        print(i, results[i][j])
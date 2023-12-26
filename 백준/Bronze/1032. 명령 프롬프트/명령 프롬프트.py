import sys 

n = int(sys.stdin.readline().rstrip())
files = []

for _ in range(n):
    f = sys.stdin.readline().rstrip()
    files.append(f)

first = files.pop()
indices = []
for f in files:
    for i in range(len(first)):
        if first[i] != f[i]:
            indices.append(i)
answer = ''
for i in range(len(first)):
    if i in indices : answer += '?'
    else: answer += first[i]

print(answer)
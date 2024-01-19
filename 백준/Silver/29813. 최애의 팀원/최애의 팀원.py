import sys

n = int(sys.stdin.readline().rstrip())
lines = []

for _ in range(n):
    name, num = sys.stdin.readline().rstrip().split()
    lines.append((name, num))

while True:
    if len(lines) == 1 : break
    cur = lines[0]
    name, num = cur
    num = int(num)

    for _ in range(num-1):
        temp = lines.pop(1)
        lines.append(temp)
        # print(lines)
    lines.pop(0)
    lines.pop(0)

print(lines[0][0])
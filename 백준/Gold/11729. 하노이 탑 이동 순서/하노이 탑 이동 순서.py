import sys

num_disk = int(sys.stdin.readline().rstrip())
cnt_move = 0
results = []

def hanoi(num_disk, x,y,z):
    if num_disk > 0:
        hanoi(num_disk-1, x,z,y)
        results.append((x,z))
        global cnt_move
        cnt_move += 1
        hanoi(num_disk-1, y,x,z)

hanoi(num_disk, 1, 2, 3)
print(cnt_move)
for result in results:
    print(result[0], result[1])